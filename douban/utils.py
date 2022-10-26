import re
def trim_text(text):
  org_text= ''.join(''.join(text[0]))
  org_text = re.sub('<[^<]+?>', '', org_text).replace('\n', '').replace('\r', '').strip()
  return org_text

