import requests
import random
import time

headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Host': 'twypage.com',
    'Referer': 'https://twypage.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

t = random.randint(1,2)
time.sleep(t)

url = "https://twypage.com/"
r1 = requests.get(url=url,headers=headers)

url = 'http://temp.check-article.cfd888.info/write_csv'

data = {'string': 'company,phone,address,na,na,na,company,phone,address,na,na,'+ str(r1)}

r = requests.post(url=url, data=data, timeout=5)
print(r.text)