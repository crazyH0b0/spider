import pandas as pd
import requests
from lxml import etree
import json
data = []
response = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
data = json.loads(result[0])
component = data['component']
caseList = component[0]['caseList']

for item in caseList:
    name = item['area']
    confirmed = item['confirmed']
    death = item['died']
    cured = item['crued']
    curConfirm = item['curConfirm']
    data.append([name, confirmed, death, cured, curConfirm])

df = pd.DataFrame(data, columns=['地区', '确诊人数', '死亡人数', '治愈人数', '现存确诊人数'])

df.to_excel('data.xlsx')

