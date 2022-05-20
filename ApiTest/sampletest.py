import requests
import json
BASE_URL = "https://reqres.in"
response = requests.get(BASE_URL + "/api/users?page=2")
#print(response)
#print(response.json())
print(json.dumps(response.json(), indent=2))
