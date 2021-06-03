import json
def compare(json1,json2):
    a=json.loads(json1)
    b=json.loads(json2)
    seta=set(a.keys())
    setb=set(b.keys())
    result = True
    if len(seta.symmetric_difference(setb))==0:

        for key in a.keys():
            if a[key]!=b[key]:

                result=False
                break

        return result
    else:
        result=False
        return  result

if __name__=='__main__':
    a={"a":1,"b":2}
    b={"b":2,"a":3}
    a=json.dumps(a)
    b=json.dumps(b)
    res=compare(a,b)
    print(res)