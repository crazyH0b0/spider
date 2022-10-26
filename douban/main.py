#豆瓣电影详情爬取
import requests
import re
def crawl():


  base_url ='https://movie.douban.com/subject/26654184/?from=showing'
  headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
      }
  res=requests.get(base_url,headers=headers)
  res.encoding='utf-8'
  page_text=res.text

  # 标题
  title_ex='<span property="v:itemreviewed">(.*?)</span>.*?<span class="year">(.*?)</span>'
  title_text=re.findall(title_ex,page_text,re.S)

  #导演
  director_ex='<a href="/celebrity/.*?" rel="v:directedBy">(.*?)</a></span></span>'
  director_text=re.findall(director_ex,page_text,re.S)

  #编剧
  scriptwriter_ex='编剧.*?<a href="/celebrity/.*?">(.*?)</a></span>'
  scriptwriter_text=re.findall(scriptwriter_ex,page_text,re.S)
  org_text= ''.join(''.join(scriptwriter_text[0]))
  org_text = re.sub('<[^<]+?>', '', org_text).replace('\n', '').replace('\r', '').strip()

  #主演
  starring_ex='主演.*?<a href="/celebrity/.*?">(.*?)</a></span>'
  starring_text=re.findall(starring_ex,page_text,re.S)
  org_text= ''.join(''.join(starring_text[0]))
  org_text = re.sub('<[^<]+?>', '', org_text).replace('\n', '').replace('\r', '').strip()

  #类型
  type_ex='<span property="v:genre">(.*?)</span>'
  type_text=re.findall(type_ex,page_text,re.S)

  #语言
  language_ex='语言:</span>(.*?)<br/>'
  language_text=re.findall(language_ex,page_text,re.S)

  #上映日期
  release_date_ex='<span property="v:initialReleaseDate".*?>(.*?)</span>'
  release_date_text=re.findall(release_date_ex,page_text,re.S)

  #片长
  duration_ex='<span property="v:runtime".*?>(.*?)</span>'
  duration_text=re.findall(duration_ex,page_text,re.S)

  #又名
  alias_ex='又名:</span>(.*?)<br/>'
  alias_text=re.findall(alias_ex,page_text,re.S)

  #IMDb链接
  IMDb_ex='IMDb.*?</span> (.*?)<br>'
  IMDb_text=re.findall(IMDb_ex,page_text,re.S)

  #豆瓣评分
  douban_score_ex='<strong class="ll rating_num".*?>(.*?)</strong>'
  douban_score_text=re.findall(douban_score_ex,page_text,re.S)

  #评价人数
  comment_ex='<span property="v:votes">(.*?)</span>'
  comment_text=re.findall(comment_ex,page_text,re.S)
  #简介
  introduction_ex='<span property="v:summary".*?>(.*?)</span>'
  introduction_text=re.findall(introduction_ex,page_text,re.S)
  


crawl()