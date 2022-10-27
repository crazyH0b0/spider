#豆瓣电影详情爬取
from ast import main
import requests
import re

from lxml import etree
from utils import trim_text
map=[]
# 排名 名字 链接 评分
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
    tree=etree.HTML(page_text)
    lis=tree.xpath('//ol/li')
    for li in lis:
      rank=li.xpath('.//em/text()')[0]
      title=li.xpath('.//span[@class="title"]/text()')[0]
      link=li.xpath('.//a/@href')[0]
      score=li.xpath('.//span[@class="rating_num"]/text()')[0]
      print('---'.join([rank,title,score,link]))
  
get_url()