import requests
import json
import string
import random


base_url = "http://127.0.0.1:5000"

def get_requests():
    url = base_url + "/"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()

    print(json.dumps(json_data, indent=4))

def post_request():
    url = base_url + "/"
    headers = {"Content-Type":"application/json"}
    data = {
        "id":10,
        "name":"mi"
    }
    response = requests.post(url,  json=data,headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    print(json.dumps(json_data))


def putting_request():
    url = base_url + "/"
    headers = {"Content-Type":"application/json"}
    updated_data = {
        "id":10,
        "name":"mi"
    }
    response = requests.put(url,json=updated_data, headers=headers)
    json_data = response.json()
    print(json.dumps(json_data, indent=4))

def deleting_request():
    url = base_url + "/del/1"
    headers = {"Content-Type":"application/json"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print("Resource deleted successfully.")
    else:
        print("Failed to delete the resource. Status code:", response.status_code)
        print("Response content:", response.content)


#post_request()
get_requests()
#putting_request()
#deleting_request()
