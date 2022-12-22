import pandas as pd
import requests
from lxml import etree
import json
dict = []
response = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
caseList = json.loads(result[0])['component'][0]['caseList']
for item in caseList:
        data = {'地区': item['area'],'累计确诊': item['confirmed'],'死亡': item['died'],'治愈': item['crued'],'现有确诊': item['curConfirm'], '累计确诊增量': item['confirmedRelative'], '死亡增量': item['diedRelative'], '治愈增量': item['curedRelative'], '现有确诊增量': item['curConfirmRelative'], '死亡增量': item['diedRelative'],'治愈增量': item['confirmedRelative'], '现有确诊增量': item['curConfirmRelative'] }
        dict.append(data)
df = pd.DataFrame(dict)
df.to_excel('中国.xlsx',index=False)

