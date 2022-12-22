#豆瓣电影详情爬取
from ast import main
import requests
import re

from lxml import etree
from utils import trim_text
def get_data():
  base_url='https://movie.douban.com/top250?start={}&filter='
  proxies = {
  "http": "121.196.152.42:80",
}
  for i in range(0,250,25):
    url=base_url.format(i)
    headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
      }
    cookie={
        'cookie':'SINAGLOBAL=2412971373627.6636.1658576914744; UOR=,,cn.bing.com; _s_tentry=-; Apache=8684915686252.641.1666751496429; ULV=1666751496447:15:4:2:8684915686252.641.1666751496429:1666709173077; SCF=Auk5dYIAtxD6dLLPDqsHeCRndcnBqB_IkHC0rHXs-DqcWyrGWJ_sQlu1_0hjM5lhAirbnDGCdEzMagytmwdRSIM.; SUB=_2A25OXOznDeRhGeNG7VQX-CbKzDiIHXVtKFkvrDV8PUJbmtAKLUHukW9NSycZmUBrbsXf1xKUUg0E9GQOUNpwvLO9; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFIj1z4HBfdW_32x4qd6Oae5JpX5K-hUgL.Fo-RSoqc1hncS0B2dJLoIEXLxKqLBoeLBK-LxK-LBKBLBoBLxKnLB.BLBKqLxKqL122LB-zLxKnL1K5LBKnt; ALF=1698287670; SSOLoginState=1666751671'
    }
    res=requests.get(url,headers=headers,proxies=proxies,cookies=cookie)
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
  
get_data()



