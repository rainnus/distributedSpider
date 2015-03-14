import json

str = file('my.json', 'r')
jinfo = str.read().decode('gbk')
info = json.dumps(jinfo, ensure_ascii=False, indent=2)
print info