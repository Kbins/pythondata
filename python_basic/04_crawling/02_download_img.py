# url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=vlzkth#

import urllib.request
import urllib.parse

url = 'https://search.naver.com/search.naver'
values = {
    'where':'nexearch',
    'sm':'top+hty',
    'fbm':'1',
    'ie':'utf8',
    'quert':'여름바다'
}

param = urllib.parse.urlencode(values)
url = url + '?' + param
print(url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)