import requests
import random

t = random.randint(1,300)
time.sleep(t)

req = requests.Session()
url = 'http://temp.check-article.cfd888.info/write_csv'

# �d�߰Ѽ�
data = {'string': '���q,�q��,�a�},na,na,na,���q,�q��,�a�},na,na,na'}

r = req.post(url=url, data=data, timeout=5)
print(r.text)