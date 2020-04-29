import requests
import json
def find_recipe(arr):
    urls="http://www.recipepuppy.com/api/"
    params={'i':arr}
    r=requests.get(url=urls,params=params)
    return r.status_code
    data=json.loads(r.text)
    return data["title"]

arr='onion,garlic'

print(find_recipe(arr))
