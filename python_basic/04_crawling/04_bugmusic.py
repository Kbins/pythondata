
import urllib.request
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')
# print(soup)

# result = soup.select('span.mask img')
# img = []
# for item in result:
#     img.append(item['src'])
# print(img)


titlelist = []
title = soup.select('p.title a')
for item in title:
    titlelist.append(item.string)
# print(titlelist)


artist = soup.select('p.artist > a:nth-of-type(1)')

# print(len(artist))
artistlist = []
for item in artist:
    artistlist.append(item.string)
print(list(zip(titlelist, artistlist)))

# artist =soup.select('p.artist')
# print(len(artist))
# for item in artist:
#     artist.append(item.get_text())