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
  for i in text:
    inner_url='https://so.gushiwen.cn/'+str(i[0])
    inner_res=requests.get(inner_url)
    inner_res.encoding='utf-8'
    inner_text=inner_res.text
    ex1='<div class="contson" id=.*?>.*?<div class="contson" id=.*?>(.*?)</div>'
    org_text=re.findall(ex1,inner_text,re.S)
    org_text= ''.join(''.join(org_text))
    org_text = re.sub('<[^<]+?>', '', org_text).replace('\n', '').strip()
    with open("text.txt", "a",encoding='utf-8') as fs:  
      fs.write(str(i[1])+'  '+str(i[2])+'  '+org_text+' '+'https://so.gushiwen.cn/'+str(i[0])+'\n')  
      # fs.close()


