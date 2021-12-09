import requests
import json

def test_GETapi():
    url = "https://reqres.in/api/users?page=2"

    resp = requests.get(url)
    print(resp.status_code)
    assert resp.status_code == 200