import requests
from bs4 import BeautifulSoup
import re



url = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'
# rel =  urllib.request.urlopen(url)
soup = BeautifulSoup(url,'lxml')

# # print(soup)
# titlelist = []
# title = soup.select('td.title a')
# for item in title:
#     titlelist.append(item.string)
# print(titlelist)
reviewlist = []
for i in range(1,11):
    print(url.format(i))
    res = requests.get(url.format(i)).text
    #print(res)
    soup = BeautifulSoup(res,'lxml')
    table = soup.find('table',class_='list_netizen')
    for i,r in enumerate(table.select('tbody tr')):
        # print(i)
        # print(r)
        for j,c in enumerate(r.find_all('td')):
            if j==0:
                recode = int(c.text)
                print('글번호:',recode)
            elif j == 1:
                recode1 = c.select_one('a').text.strip()
                print('영화제목:',recode1)
                recode2 = c.select_one('em').text
                print('영화평점:',recode2)
                recode3 = c.text
                recode3 = recode3.replace(recode1,'')
                recode3 = recode3.replace('신고','')
                # recode3 = re.sub(패턴,바꿀문자열,원문자열)
                recode3 = re.sub('별점 = 총 10점 중[0-9]{1,2}','',recode3).strip()
                print(recode3)
                try:
                    movie_dic={
                        '제목':recode1,
                        '평점':recode2,
                        '감상평':recode3
                    }
                    reviewlist.append(movie_dic)
                except:
                    pass
print(reviewlist)







