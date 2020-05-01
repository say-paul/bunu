import requests
import json
def find_recipe(a):
    urls="http://www.recipepuppy.com/api/"
    params={'i':a}
    r=requests.get(url=urls,params=params)
    print(r.status_code)
    data=json.loads(r.text)
    a = list(a.split(','))
    count,index=0,0
    extra=[]
    for i,result in enumerate(data["results"]):
        ingre = list(result["ingredients"].split(','))
        diff_a = len(list(set(a).difference(ingre)))
        if i == 0:
            count = diff_a
            index = i
        if diff_a < count:
            index = i
 
    return ({'title': data["results"][index]['title'], 'indg': data["results"]
                          [index]['ingredients'], 'link': data["results"][index]["href"]})
    

a ='garlic,chicken'

print(find_recipe(a))
