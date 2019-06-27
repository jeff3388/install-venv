import requests
import random

t = random.randint(1,300)
time.sleep(t)

req = requests.Session()
url = 'http://temp.check-article.cfd888.info/write_csv'

# 查詢參數
data = {'string': '公司,電話,地址,na,na,na,公司,電話,地址,na,na,na'}

r = req.post(url=url, data=data, timeout=5)
print(r.text)