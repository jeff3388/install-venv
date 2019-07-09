from bs4 import BeautifulSoup
import datetime
import requests
import random
import time
import re

datetime_dt = datetime.datetime.today()
datetime_str = datetime_dt.strftime("%Y-%m-%d") # today date transfer to sting format

# crawler main program
def crawler(web_url,headers,datetime_str):
    res = requests.get(url=web_url,headers=headers,timeout=15).content
    soup = BeautifulSoup(res,"html.parser")
    title_class = soup.find("title")
    info = soup.find_all("p")

    title = title_class.text.split("-")[0] # company name

    # company information
    info_ls = []
    for i in info:
        i = i.text
        info_ls += [i]
    
    
    # company #
    if len(title) > 2:
        company_name_ls = title
    elif len(title) < 2:
        company_name_ls = "Na"

    # principal #
    try:
        p2 = info_ls[1].find("負責人")
        
        if p2 != -1:
            n2 = "".join(re.findall("負責人:.*，",info_ls[1])).replace("地\u3000\u3000址","").split(":")[1].split("，")[0]
            if n2 != "":
                principal_ls = n2
            else:
                principal_ls = "Na"
        else:
            principal_ls = "Na"
    except:
        principal_ls = "Na"

    # phone #
    try:
        p3 = info_ls[0].replace("\u3000\u3000","").find("電話")
        if p3 != -1:
            n3 = "".join(re.findall("\d{2,3}-\d{8,10}",info_ls[0].replace("\u3000\u3000","")))
            if n3 != '':
                phone_ls = n3
            else:
                phone_ls = "Na"
        else:
            phone_ls = "Na"
    except:
        phone_ls = "Na"

    # uniform_numbers #
    q1 = info_ls[0].find("統一編號")
    if q1 != -1:
        m1 = "".join(re.findall("統一編號：.*",info_ls[0])).replace("地\u3000\u3000址","").split("：")[1].replace(" ","")
        if m1 != "":
            uniform_numbers_ls = m1
        else:
            uniform_numbers_ls = "Na"
    else:
        uniform_numbers_ls = "Na"

    # address #
    q2 = info_ls[0].find("地　　址")
    if q2 != -1:
        m2 = "".join(re.findall("地　　址：.*電　　話",info_ls[0])).replace("電　　話","").replace("\u3000\u3000","").split("：")[1].replace(" ","")
        if m2 != "":
            address_ls = m2
        else:
            address_ls = "Na"
    else:
        address_ls = "Na"

    # city #
    q3 = info_ls[0].find("縣　　市")
    if q3 != -1:
        m3 = "".join(re.findall("縣　　市：.*登記機關",info_ls[0])).replace("登記機關","").replace("\u3000\u3000","").split("：")[1].replace(" ","").replace("MAIL","").replace("官方網站","")
        if m3 != "":
            city_ls = m3
        else:
            city_ls = "Na"
    else:
        city_ls = "Na"

    # registration_authority #
    q4 = info_ls[0].find("登記機關")
    if q4 != -1:
        m4 = "".join(re.findall("登記機關：.*",info_ls[0])).replace("設立日期","").replace("資本額","").replace("變更日期","").split("：")[1].replace(" ","")
        if m4 != "":
            registration_authority = m4
        else:
            registration_authority = "Na"
    else:
        registration_authority = "Na"  

    # setting_date #
    q5 = info_ls[0].find("設立日期")
    if q5 != -1:
        m5 = "".join(re.findall("設立日期：.*",info_ls[0])).replace("變更日期","").replace("資本額","").split("：")[1].replace(" ","") 
        if m5 != "":
            setting_date_ls = m5
        else:
            setting_date_ls = "Na" 
    else:
        setting_date_ls = "Na"      

    # change_date #
    q6 = info_ls[0].find("變更日期")
    if q6 != -1:
        m6 = "".join(re.findall("變更日期：.*",info_ls[0])).replace("資本額","").split("：")[1].replace("所屬分類","") 
        if m6 != "":
            change_date_ls = m6
        else:
            change_date_ls = "Na"
    else:
        change_date_ls = "Na"

    # capital_amount #
    q7 = info_ls[0].find("資本額")
    if q7 != -1:
        m7 = "".join(re.findall("資本額：.*元",info_ls[0])).replace("元實收資本總額","").split("：")[1].replace(" ","") 
        if m7 != "":
            capital_amount = m7
        else:
            capital_amount = "Na"
    else:
        capital_amount = "Na"

    # kind #
    q8 = info_ls[0].find("所屬分類")
    if q8 != -1:
        m8 = "".join(re.findall("所屬分類：.*",info_ls[0])).split("：")[1].replace(" ","") 
        if m8 != "":
            kind_ls = m8
        else:
            kind_ls = "Na"
    else:
        kind_ls = "Na"
        
    company_information = company_name_ls + ";"+ principal_ls + ";"+ phone_ls + ";"+  uniform_numbers_ls + ";"+  address_ls + ";"+  city_ls + ";"+  registration_authority + ";"+  setting_date_ls + ";"+  change_date_ls + ";"+  capital_amount + ";"+ kind_ls + ";" + datetime_str + ";"
    
    return company_information

headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Host': 'twypage.com',
    'Referer': 'https://twypage.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# t = random.randint(1,60)
# time.sleep(t)

respones = requests.get("http://temp.check-article.cfd888.info/yp-url")
url_ls = respones.text.split(';')

com_info = []

for url in url_ls:
    company_information = crawler(url,headers,datetime_str)
    com_info += [company_information]

info = ";".join(com_info)
# post api
url = 'http://temp.check-article.cfd888.info/write_csv'

data = {'string': info}

r = requests.post(url=url, data=data, timeout=5)
print(r.text)