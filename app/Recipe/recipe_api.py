import requests
from flask import jsonify
def find_recipe(arr):
    urls="http://www.recipepuppy.com/api/"
    params={'ingredient':arr}
    r=requests.get(url=urls)
    data=jsonify(r)
    return data

#arr=['onion','garlic']

#print(find_recipe(arr))
