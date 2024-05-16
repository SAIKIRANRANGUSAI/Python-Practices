import json

import requests

base_url = "http://127.0.0.1:5000"

def getting():
    url = base_url + "/"
    response = requests.get(url)
    assert response.status_code ==200
    json_data = response.json()
    print(json.dumps(json_data, indent=2))

def posting():
    url = base_url + "/p"
    data = {
        "name":"rsj",
        "age":23,
        "phonenumber":787688798
    }
    response = requests.post(url,json=data)
    assert response.status_code == 201
    json_data = response.json()
    print(json_data)

def putting():
    url = base_url + "/pu/20"
    data = {
        "id":20,
        "name":"rskkkk",
        "age":23,
        "phonenumber":787688798
    }
    response = requests.put(url, json=data)
    updated_data = response.json()
    print(updated_data)


import requests


def deleting():
    url = base_url + "/d/20"
    response = requests.delete(url)
    if response.status_code == 200:
        print("DELETE request successful.")
    else:
        print("DELETE request failed with status code:", response.status_code)


deleting()

posting()
getting()
putting()
deleting()