import requests
from utils.config import BASE_URL_API, HEADERS

def test_registration_all_fields():
    url = f"{BASE_URL_API}/register"
    payload = {
        "name": "João Silva",
        "email": "joao@example.com",
        "password": "Senha@123",
        "phone": "123456789"
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["message"] == "Cadastro realizado com sucesso"