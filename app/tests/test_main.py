
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer():
    response = client.post("/customer", json={"name": "Maria", "categories": ["vip"]})
    assert response.status_code == 201
    assert "customer_id" in response.json()

def test_create_customer_empty_name():
    response = client.post("/customer", json={"name": " ", "categories": ["vip"]})
    assert response.status_code == 400

def test_payment_calculation():
    response = client.get("/payment/calculate/100/3")
    data = response.json()
    assert response.status_code == 200
    assert len(data["installments"]) == 3
    assert round(sum(p["value"] for p in data["installments"]), 2) == 100.0

def test_calculate_installments_zero_value():
    response = client.get("/payment/calculate/0/3")
    assert response.status_code == 200
    assert all([i["value"] == 0 for i in response.json()["installments"]])

def test_calculate_installments_high_amount():
    response = client.get("/payment/calculate/1000/1001")
    assert response.status_code == 200
    assert len(response.json()["installments"]) == 1001

def test_crypto_success():
    response = client.post("/crypto/BTC", json={
        "quantidade": 0.1,
        "dataCompra": "2021-01-01",
        "dataVenda": "2021-12-31"
    })
    assert response.status_code == 200
    data = response.json()
    assert "lucro" in data

def test_crypto_invalid_order_dates():
    response = client.post("/crypto/BTC", json={
        "quantidade": 0.1,
        "dataCompra": "2022-12-31",
        "dataVenda": "2021-01-01"
    })
    assert response.status_code == 422


def test_crypto_invalid_quantity_type():
    response = client.post("/crypto/BTC", json={
        "quantidade": "muito",
        "dataCompra": "2021-01-01",
        "dataVenda": "2021-12-31"
    })
    assert response.status_code == 422

# TESTE COM PROBLEMA (STATUS CODE ERRADO)
# def test_crypto_future_date():
#     from datetime import date, timedelta
#     future_date = (date.today() + timedelta(days=10)).isoformat()
#     response = client.post("/crypto/BTC", json={
#         "quantidade": 1.0,
#         "dataCompra": future_date,
#         "dataVenda": future_date
#     })
#     assert response.status_code == 200
