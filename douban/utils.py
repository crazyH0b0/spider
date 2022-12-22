import re
def trim_text(text):
  # 判断text是否有内容
  if len(text) >= 0:
    # 返回text[0]的值
    org_text= ''.join(''.join(text[0]))
    org_text = re.sub('<[^<]+?>', '', org_text).replace('\n', '').replace(u'\u3000',u'').replace('\r', '').strip()
    return org_text
  else:
    return '无'




