import requests
import re
import pymysql
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='webdb')
cursor = db.cursor()
base_url = 'http://127.0.0.1:5500/2/web_demo.html'
res = requests.get(base_url)
res.encoding ='utf-8'
page_text = res.text 
ex='<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>'
text = re.findall(ex,page_text,re.S)
for index,value in enumerate(text):
  if index != 0:
    try:
      sql = 'insert into search_index(id,keyword,number) values(%s,%s,%s)'
      cursor.execute(sql,value)
      db.commit()
    except:
      db.rollback()
db.close()




