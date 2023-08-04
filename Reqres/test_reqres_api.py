import pytest
import requests

url_1 = "https://reqres.in/api/users"
url_2 = "https://reqres.in/api/users/2"

def test_01_create_user():
    payloads = {
        "name": "Fairuz Hanif Rabbani",
        "job": "Software Quality Assurance"
    }
    response = requests.post(url_1, json=payloads, headers={"Content-Type": "application/json"})
    response_body = response.json()
    # Verify
    assert response.status_code == 201, "Response code should be 201"
    assert response_body["name"] == "Fairuz Hanif Rabbani"
    assert response_body["job"] == "Software Quality Assurance"

def test_02_update_user():
    payloads = {
        "name": "Erlinda Lutfitasari",
        "job": "Data Engineer"
    }
    response = requests.put(url_2, json=payloads, headers={"Content-Type": "application/json"})
    response_body = response.json()
    # Verify
    assert response.status_code == 200, "Response code should be 200"
    assert response_body["name"] == "Erlinda Lutfitasari"
    assert response_body["job"] == "Data Engineer"


def test_03_delete_user():
    response = requests.delete(url_2, headers={"Content-Type": "application/json"})
    # Verify
    assert response.status_code == 204, "Response code should be 204"
