import requests
import re
base_url='https://so.gushiwen.cn/mingju/default.aspx?p={}&c=&t='
for i in range(1,21):
  text_url=base_url.format(i)
  res=requests.get(text_url)
  res.encoding='utf-8'
  page_text=res.text
  ex='<a style=" float:left;" .*? href="(.*?)">(.*?)</a>.*?span.*?<a.*? href=.*?>(.*?)</a.*?>'
  text=re.findall(ex,page_text,re.S)
  for item in text:
    with open("test.txt", "a",encoding='utf-8') as fs:  
      fs.write(str(item[1])+'  '+str(item[2])+'  '+'https://so.gushiwen.cn/'+str(item[0])+'\n')  
      # fs.close()
# <a style=" float:left;" target="_blank" href="/mingju/juv_56cd8fe503c4.aspx">十年寒窗无 
# 人问，一举成名天下知。</a>