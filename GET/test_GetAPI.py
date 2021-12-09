import requests

def test_GET():
    url = "https://reqres.in/api/users?page=2"

    resp = requests.get(url)
    assert resp.status_code == 200

def test_GET2():
    url = "https://reqres.in/api/users/2"

    resp = requests.get(url)
    assert resp.status_code == 200