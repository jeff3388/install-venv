import requests
import random
import time

t = random.randint(1,2)
time.sleep(t)

req = requests.Session()
url = 'http://temp.check-article.cfd888.info/write_csv'

data = {'string': 'company,phone,address,na,na,na,company,phone,address,na,na,na'}

r = req.post(url=url, data=data, timeout=5)
print(r.text)