import requests
import json


class Webrequests():

    def get(self,url,data,headers):
        try:
            r = requests.get(url,params=data,headers=headers)
            print(url,data,headers)
            json_r = r.json()

            print("Test执行结果：",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))


    def post(self,url,data,headers):
        try:
            r = requests.post(url,data=data,headers=headers)
            json_r = r.json()
            print("Test执行结果：",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))
    def post_json(self,url,data,headers):
        try:
            data = json.dumps(data)
            r = requests.post(url,json=data,headers=headers)
            r.encoding = 'utf-8'
            json_r = r.json()
            print("Test执行结果：",json_r)
            return json_r
        except BaseException as e:
            print("请求失败！",str(e))

    def run_main(self, method,url,data,headers):
        result = None
        if method == 'post':
            result = self.post(url,data,headers)
        elif method == 'get':
            result = self.get(url,data,headers)
        elif method == 'post_json':
            result = self.post_json(url, data, headers)
        else:
            print("method值错误！！！")
        return result

if __name__=="__main__":
    # d = {'output': 'json',
    #       'ak': 'Wy2yHooxcqqYHUmql88EYTYfq82CHQTH',
    #       'address': '电投大厦',
    #      'city': '北京'}
    # r=Webrequests().run_main('post','http://api.map.baidu.com/geocoder/v2/',d,{})
    # print(r)


    data = {'name': 'huxiaoyan'}
    r = Webrequests().run_main('post_json', 'http://httpbin.org/post', data, {})
    print(r)




