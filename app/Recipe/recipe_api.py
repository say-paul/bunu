import requests
import json
def find_recipe(a):
    urls="http://www.recipepuppy.com/api/"
    a=list(a.split(','))
    params={'i':a}
    r=requests.get(url=urls,params=params)
    # return r.status_code
    data=json.loads(r.text)
   # print(data["results"])
    #return len(array)
    #ingredient=list()
    #return len(data["results"])

    count=0
    extra=[]
    for i in range(len(data["results"])):
        ingre=list(data["results"][i]["ingredients"].split(','))
        for j in range(len(a)):
            if a[j] in ingre:
                count+=1
        extra.append(len(ingre)-count)
        count=0 
    print(extra)
    m=min(extra)
    final=[]
    for i in range(len(extra)):
        if m==extra[i]:
            final.append({'title':data["results"][i]['title'],'link':data["results"][i]["href"]})
    return final
    

a ='garlic,chicken'

print(find_recipe(a))
