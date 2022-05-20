import requests
import json

BASE_URL = "https://reqres.in"
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put(BASE_URL + "/api/users/2", data=payload)
print(response.json())
