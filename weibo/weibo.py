import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
def get_hot_search():
    str=''
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    cookie={
        'cookie':'SINAGLOBAL=2412971373627.6636.1658576914744; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFIj1z4HBfdW_32x4qd6Oae5JpX5KMhUgL.Fo-RSoqc1hncS0B2dJLoIEXLxKqLBoeLBK-LxK-LBKBLBoBLxKnLB.BLBKqLxKqL122LB-zLxKnL1K5LBKnt; ALF=1698553481; SSOLoginState=1667017482; SCF=Auk5dYIAtxD6dLLPDqsHeCRndcnBqB_IkHC0rHXs-Dqcq1qJcZbeK46aRAiywLlVYVpzIZNFFXM7rtqm9jUUOKk.; SUB=_2A25OWNtaDeRhGeNG7VQX-CbKzDiIHXVtLEuSrDV8PUNbmtAKLWmskW9NSycZmTb2BQQ19BuQ3DMoTm70QJOE3zyl; _s_tentry=-; Apache=2230753194690.487.1667026548590; ULV=1667026548601:17:6:4:2230753194690.487.1667026548590:1666839941730'
    }
    response = requests.get(url, headers=headers,cookies=cookie)
    response.encoding = 'utf-8'
    page_text = response.text
    ex = '<td class=".*?ranktop">(.*?)</td>.*?<td class=".*?">.*?<a href="/(.*?)" target="_blank">(.*?)</a>.*?<span> (.*?)</span>'
    hot_list = re.findall(ex, page_text, re.S)
    for hot in hot_list:
        str+=hot[0]+'--'+hot[2]+'--'+hot[3]+'--'+hot[1]+'\n'
    return str
# 发送邮箱
def mail(text='微博热搜'):
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="2718881989@qq.com"    #用户名
    mail_pass="rpfjcdgchpiodcjf"   #口令
    sender = '2718881989@qq.com'
    receivers = ['1327185450@qq.com'] 
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("微博热搜", 'utf-8')
    message['To'] =  Header("微博热搜", 'utf-8')
    subject = '微博热搜'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
def job(n):
    while True:
        mail(get_hot_search())
        time.sleep(n)
job(20)


