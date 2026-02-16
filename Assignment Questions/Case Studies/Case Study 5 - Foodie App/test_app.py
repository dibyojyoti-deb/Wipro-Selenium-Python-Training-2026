import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

restaurant_id = None
user_id = None
order_id = None
dish_id = None


def test_01_register_restaurant():
    global restaurant_id
    data = {
        "name": "Food Hub",
        "category": "Veg",
        "location": "Delhi",
        "contact": "9999999999"
    }
    response = requests.post(f"{BASE_URL}/restaurants", json=data)
    assert response.status_code == 201
    restaurant_id = response.json()["id"]


def test_02_duplicate_restaurant():
    data = {
        "name": "Food Hub",
        "category": "Veg",
        "location": "Delhi",
        "contact": "9999999999"
    }
    response = requests.post(f"{BASE_URL}/restaurants", json=data)
    assert response.status_code == 409


def test_03_view_restaurant():
    response = requests.get(f"{BASE_URL}/restaurants/{restaurant_id}")
    assert response.status_code == 200


def test_04_update_restaurant():
    response = requests.put(
        f"{BASE_URL}/restaurants/{restaurant_id}",
        json={"location": "Mumbai"}
    )
    assert response.status_code == 200


def test_05_disable_restaurant():
    response = requests.put(
        f"{BASE_URL}/restaurants/{restaurant_id}/disable"
    )
    assert response.status_code == 200


def test_06_add_dish():
    global dish_id
    data = {
        "name": "Pizza",
        "type": "Veg",
        "price": 250
    }
    response = requests.post(
        f"{BASE_URL}/restaurants/{restaurant_id}/dishes",
        json=data
    )
    assert response.status_code == 201
    dish_id = response.json()["id"]


def test_07_update_dish():
    response = requests.put(
        f"{BASE_URL}/dishes/{dish_id}",
        json={"price": 300}
    )
    assert response.status_code == 200


def test_08_toggle_dish_status():
    response = requests.put(
        f"{BASE_URL}/dishes/{dish_id}/status",
        json={"enabled": False}
    )
    assert response.status_code == 200


def test_09_delete_dish():
    response = requests.delete(f"{BASE_URL}/dishes/{dish_id}")
    assert response.status_code == 200


def test_10_user_registration():
    global user_id
    data = {
        "name": "DJ",
        "email": "DJ@test.com"
    }
    response = requests.post(f"{BASE_URL}/users/register", json=data)
    assert response.status_code == 201
    user_id = response.json()["id"]


def test_11_duplicate_user():
    data = {
        "name": "DJ",
        "email": "DJ@test.com"
    }
    response = requests.post(f"{BASE_URL}/users/register", json=data)
    assert response.status_code == 409


def test_12_place_order():
    global order_id
    data = {
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "dishes": []
    }
    response = requests.post(f"{BASE_URL}/orders", json=data)
    assert response.status_code == 201
    order_id = response.json()["id"]


def test_13_view_user_orders():
    response = requests.get(f"{BASE_URL}/users/{user_id}/orders")
    assert response.status_code == 200


def test_14_view_restaurant_orders():
    response = requests.get(
        f"{BASE_URL}/restaurants/{restaurant_id}/orders"
    )
    assert response.status_code == 200


def test_15_give_rating():
    data = {
        "order_id": order_id,
        "rating": 5,
        "comment": "Excellent"
    }
    response = requests.post(f"{BASE_URL}/ratings", json=data)
    assert response.status_code == 201


def test_16_admin_approve_restaurant():
    response = requests.put(
        f"{BASE_URL}/admin/restaurants/{restaurant_id}/approve"
    )
    assert response.status_code == 200


def test_17_admin_disable_restaurant():
    response = requests.put(
        f"{BASE_URL}/admin/restaurants/{restaurant_id}/disable"
    )
    assert response.status_code == 200


def test_18_admin_view_orders():
    response = requests.get(f"{BASE_URL}/admin/orders")
    assert response.status_code == 200
