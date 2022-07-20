
import urllib.request
url = '이미지 url주소'
savename = 'test.png'
urllib.request.urlretrieve(url,savename)


#-----------------------------------------------------------------------------------
from urllib import request

url = 'https://www.naver.com/'
mem = request.urlopen(url).read()
print(mem.decode('utf-8'))


#-----------------------------------------------------------------------------------
import requests

r = requests.get(url)
# print(r.text)
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
print(r.encoding)
print(r.json())


