import pytest
import allure
from main import BaseRequest
from models import User, Order

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


@allure.feature("User Management")
def test_user_management():
    with allure.step("Create a new user"):
        new_user = User(
            id=1,
            username="danMark",
            firstName="Dan",
            lastName="Mark",
            email="dan@example.com",
            password="password",
            phone="1234567890",
            userStatus=1
        )
        created_user = base_request.post('user', '', new_user.model_dump())
        created_user_info = base_request.get('user', new_user.username)
        assert created_user_info['username'] == new_user.username


@allure.feature("Order Management")
def test_order_management():
    with allure.step("Create a new order"):
        new_order = Order(
            id=1,
            petId=1,
            quantity=1,
            shipDate="2024-10-14T18:30:00.000Z",
            status="placed",
            complete=True
        )
        created_order = base_request.post('store/order', '', new_order.model_dump())
        assert created_order['status'] == new_order.status

    with allure.step("Get order information"):
        order_info = base_request.get('store/order', 1)
        assert order_info['status'] == 'placed'

    with allure.step("Delete order"):
        deleted_order = base_request.delete('store/order', 1)
        assert deleted_order['message'] == str(new_order.id)

