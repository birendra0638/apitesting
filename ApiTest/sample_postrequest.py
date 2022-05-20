import requests
import json

BASE_URL = "https://reqres.in"
payload = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post(BASE_URL + "/api/users", data=payload)
print(response.json())
