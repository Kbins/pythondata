import sqllite_test6 as st

st.create_table()
while True:
    menu = input('''
    1.입력 2.수정 3.삭제 4.리스트 5.종료
    -->''')
    if menu == '1':
        st.insert_book()
    elif menu == '2':
        st.update_book()
    elif menu == '3':
        st.delete_book()
    elif menu == '4':
        st.list_book()
    elif menu == '5':
        pass
    else:
        print('잘못 입력했습니다')
    