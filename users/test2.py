import json

import requests

url="http://httpbin.org/post"
data={'name':'huxiaoyan'}
r=requests.post(url,json=data)
print(r.status_code)
print(type(r.json()['data']))
d=r.json()['data']
d1=json.loads(d)
print(d1['name'])
assert d1['name']=='huxiaoyan'
import requests
url="http://httpbin.org/post"
data={'name':'huxiaoyan'}
r=requests.post(url,data=data)
print( r.json())
