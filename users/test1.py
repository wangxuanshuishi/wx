import requests
import json


url = 'http://api.map.baidu.com/geocoder/v2/'
d={'output':'json',
   'ak':'Wy2yHooxcqqYHUmql88EYTYfq82CHQTH',
   'address':'电投大厦',
   'city':'北京'}
r = requests.get(url,params=d)
d= r.json()
print(d)
