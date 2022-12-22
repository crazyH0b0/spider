#豆瓣电影详情爬取
from ast import main
import requests
import re
import sys

from utils import trim_text
map=[]
def crawl(url):
  base_url =url
  headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
      }
  cookie={
        'cookie':'ll="118309"; bid=MpZd7t2EZGU; __gads=ID=fbe757ea765eb266-221f968b4dd50086:T=1658500015:RT=1658500015:S=ALNI_MaBhPttSzuvoj9gj6m6Y5SNd3EvLQ; douban-fav-remind=1; ct=y; dbcl2="249472745:8bu1vbNaQN0"; ck=P3Rg; __utmc=30149280; __utmz=30149280.1666973705.105.20.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __gpi=UID=000007f930fa24bb:T=1658500015:RT=1666973704:S=ALNI_MYLgHpAYGZEHyNQua5jbu_XBhNNsQ; push_noty_num=0; push_doumail_num=0; __utma=30149280.612397039.1658500005.1666973705.1666976709.106; __utmb=30149280.0.10.1666976709'
    }
  res=requests.get(base_url,headers=headers,cookies=cookie)
  res.encoding='utf-8'
  page_text=res.text

  #排名
  ex='<span class="top250-no">(.*?)</span>'
  
  rank=re.findall(ex,page_text,re.S)[0] if len(re.findall(ex,page_text,re.S))>0 else '无'

  # 标题
  # title_ex='<span property="v:itemreviewed">(.*?)</span>.*?<span class="year">(.*?)</span>'
  title_ex='<span property="v:itemreviewed">(.*?)</span>'
  title_text=re.findall(title_ex,page_text,re.S)[0] if len(re.findall(title_ex,page_text,re.S))>0 else '无'

  #导演
  director_ex='<a href="/celebrity/.*?" rel="v:directedBy">(.*?)</a></span></span>'
  director_text=trim_text(re.findall(director_ex,page_text,re.S))
  #编剧
  scriptwriter_ex='编剧.*?<a href="/celebrity/.*?">(.*?)</a></span>'

  scriptwriter_text=trim_text(re.findall(scriptwriter_ex,page_text,re.S)) if len(re.findall(scriptwriter_ex,page_text,re.S))>0 else '无'
 
  #主演
  starring_ex='主演.*?<a href="/celebrity/.*?">(.*?)</a></span>'

  starring_text=trim_text(re.findall(starring_ex,page_text,re.S)) if len(re.findall(starring_ex,page_text,re.S))>0 else '无'

  #类型
  type_ex='<span property="v:genre">(.*?)</span>'

  type_text=trim_text(re.findall(type_ex,page_text,re.S)) if len(re.findall(type_ex,page_text,re.S))>0 else '无'
  #语言
  language_ex='语言:</span> (.*?)<br/>'
  language_text=re.findall(language_ex,page_text,re.S)[0] if len(re.findall(language_ex,page_text,re.S))>0 else '无'
  #上映日期
  release_date_ex='<span property="v:initialReleaseDate".*?>(.*?)</span>'

  release_date_text=re.findall(release_date_ex,page_text,re.S)[0] if len(re.findall(release_date_ex,page_text,re.S))>0 else '无'
 
  #制片国家地区
  country_ex='制片国家/地区:</span> (.*?)<br/>'
    #三元运算符
  country_text=re.findall(country_ex,page_text,re.S)[0] if len(re.findall(country_ex,page_text,re.S))>0 else '无'

  #片长
  duration_ex='<span property="v:runtime".*?>(.*?)</span>'

  duration_text=re.findall(duration_ex,page_text,re.S)[0] if len(re.findall(duration_ex,page_text,re.S))>0 else '无'

  #又名
  alias_ex='又名:</span> (.*?)<br/>'
  alias_text=re.findall(alias_ex,page_text,re.S)[0] if len(re.findall(alias_ex,page_text,re.S))>0 else ''
  #IMDb
  IMDb_ex='IMDb.*?</span> (.*?)<br>'
  IMDb_text=re.findall(IMDb_ex,page_text,re.S)[0] if len(re.findall(IMDb_ex,page_text,re.S))>0 else '无'
  #豆瓣评分
  douban_score_ex='<strong class="ll rating_num".*?>(.*?)</strong>'

  douban_score_text=re.findall(douban_score_ex,page_text,re.S)[0] if len(re.findall(douban_score_ex,page_text,re.S))>0 else '无'
  #评价人数
  comment_ex='<span property="v:votes">(.*?)</span>'

  comment_text=re.findall(comment_ex,page_text,re.S)[0] if len(re.findall(comment_ex,page_text,re.S))>0 else '无'
  #简介
  introduction_ex='<span property="v:summary".*?>(.*?)</span>'

  introduction_text= re.findall(introduction_ex,page_text,re.S)[0].replace(u'\u3000',u'').replace('\n', '').replace('\r', '').replace(" ","").replace("<br/>","").strip()  if len(re.findall(introduction_ex,page_text,re.S))>0 else '无'

  return{
    '排名':rank,
      '电影名称':title_text,
      '导演':director_text,
      '编剧':scriptwriter_text,
      '主演':starring_text,
      '类型':type_text,
      '制片国家/地区':country_text,
      '语言':language_text,
      '上映日期':release_date_text,
      '片长':duration_text,
      '又名':alias_text,
      'IMDb':IMDb_text,
      '豆瓣评分':douban_score_text,
      '评价人数':comment_text,
      '简介':introduction_text
  }

#豆瓣前250内容链接
def get_url():
  base_url='https://movie.douban.com/top250?start={}&filter='
  for i in range(0,250,25):
    url=base_url.format(i)
    headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
      }
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    page_text=res.text
    ex='<div class="hd">.*?<a href="(.*?)"'
    li_list=re.findall(ex,page_text,re.S)
    for li in li_list:
      map.append(li)
  return map
urls=get_url()
for url in urls:
  content=crawl(url)
  #写入文件
  with open("电影.txt", "a",encoding='utf-8') as fs:  
      fs.write(str(content)+'\r\n')
  
#步骤
#1.获取豆瓣前250电影的链接，存入列表，通过循环遍历然后获取每个电影的详情页链接，正则匹配
