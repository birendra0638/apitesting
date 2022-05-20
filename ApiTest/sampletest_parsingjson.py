# API testing with Python Part 2: Adding Query parameters to requests.
import requests
import json

BASE_URL = "https://reqres.in"
param = {'page': 2}
response = requests.get(BASE_URL + "/api/users", params=param)
# print(response)
# print(response.json())
print(json.dumps(response.json(), indent=2))
resp = response.json()
# import ipdb;ipdb.set_trace()

firstname = [d['email'] for d in resp['data']]
print(firstname)
