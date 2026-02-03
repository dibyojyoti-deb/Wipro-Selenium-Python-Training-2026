import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

@pytest.fixture
def patient_data():
    return {
        "name": "John",
        "age": 30,
        "gender": "Male",
        "disease": "Flu",
        "doctor": "Dr. Smith"
    }

def test_register_patient(patient_data):
    response = requests.post(BASE_URL, json=patient_data)
    assert response.status_code == 201

def test_get_patients():
    response = requests.get(BASE_URL)
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_multiple_patients(name):
    response = requests.post(BASE_URL, json={"name": name})
    assert response.status_code == 201

def test_negative_case():
    response = requests.post(BASE_URL, json={"age": 40})
    assert response.status_code == 400

@pytest.mark.skip(reason="Under development")
def test_skip_example():
    assert False

@pytest.mark.xfail
def test_expected_failure():
    assert False