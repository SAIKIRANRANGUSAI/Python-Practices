import requests,json

base_url = "http://127.0.0.1:5000"

def getting_data():
    url = base_url+"/"
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    print(json.dumps(json_data,indent=2))


def getting_data_by_id(id):
    url = base_url+"/"+str(id)
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    print(json.dumps(json_data,indent=2))

def posting_data_creating():
    url = base_url+"/p"
    data = {
        "name": "sairangu", "age": 45
    }
    response = requests.post(url,json=data)
    assert response.status_code == 201
    json_data = response.json()
    print(json.dumps(json_data,indent=2))

def putting(id):
    url = base_url+"/put/"+str(id)
    ss = {
        "name":"saikiranranguuuuuu",
        "age":76
    }
    response = requests.put(url,json=ss)
    response.raise_for_status()
    assert response.status_code == 200
    json_data = response.json()
    print(json.dumps(json_data,indent=2))


def deleting(id):
    url = base_url+"/d/"+str(id)
    response = requests.delete(url)
    assert response.status_code==200
    json_data = response.json()
    print(json.dumps(json_data,indent=3))

deleting(2)