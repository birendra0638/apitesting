import requests
import json


def test_add_mul_students():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    f = open("F:/Python_files/API_Test/add_student.json")
    json_request = json.loads(f.read())
    response = requests.post(api_url, json_request)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 201
