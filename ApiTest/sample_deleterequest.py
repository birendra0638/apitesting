import requests
import json

BASE_URL = "https://reqres.in"

response = requests.delete(BASE_URL + "/api/users/2")
print(response.status_code)
