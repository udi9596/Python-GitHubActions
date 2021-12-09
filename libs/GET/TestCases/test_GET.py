import requests
import json

def test_GETapi():
    url = "https://reqres.in/api/users?page=2"

    resp = requests.get(url)
    assert resp.status_code == 200