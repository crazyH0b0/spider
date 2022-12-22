import pandas as pd
import requests
from lxml import etree
import json
response = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
areaList = json.loads(result[0])['component'][0]['globalList']
data = [ [item['country'], item['confirmed'], item['died'], item['crued'], item['curConfirm'], item['confirmedRelative']]for caseList in areaList for item in caseList['subList']]
df = pd.DataFrame(data, columns=['国家', '累计确诊', '死亡', '治愈', '现有确诊', '累计确诊增量'])
df.to_excel('国外.xlsx',index=False)





















