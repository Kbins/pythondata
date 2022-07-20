#웹으로 가능하나 번거롭다
#pip install streamlit 1.설치
#pip install streamlit-chat 2.설치
#실행 streamlit run python_basic\12_health_chatbot\chatbot.py 경로가 다를때 상대경로~
import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json


# st.write("""
# heloo world!우~효~
# """)

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model              

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('python_basic/12_health_chatbot/wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('심리상담 챗봇')
st.markdown('[참고사이트](https://streamlit.io/)')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []  #저장하는 용도

with st.form('form',clear_on_submit=True):  #clear_on_submit 정리해주는 역할
    user_input = st.text_input('상담내용 입력 : ','')
    submitted =  st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)
    df['distance'] = df['embedding'].map(lambda x:cosine_similarity([embedding],[x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])

for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i],is_user=True,key=str(i)+'_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i],key=str(i)+'_bot')
