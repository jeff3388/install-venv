import sqlite3
import datetime
import csv
import time
import re

datetime_dt = datetime.datetime.today()# 獲得當地時間
datetime_str = datetime_dt.strftime("%Y-%m-%d")

db_name = r'C:\Users\admin\Desktop\after_baidu.db'
con = sqlite3.connect(db_name) 
c = con.cursor() # 建立連線物件
 
# 由大到小(降冪)獲取第一筆資料
def get_data(table_name):
    with con:
        c.execute('SELECT * FROM '+ "'" + table_name + "'" )
        rows = c.fetchall()
        number = str(len(rows))
        
        return number

def write_csv(datetime_str,number):
    # 開啟輸出的 CSV 檔案
    with open(r'C:\Users\admin\Desktop\test.csv', 'a', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入另外幾列資料
        writer.writerow([datetime_str, number])
    
number = get_data('baidu_table')
write_csv(datetime_str,number)