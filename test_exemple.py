    # test_example.py
import pytest
import allure

@allure.feature("Authentication")
@allure.story("Login Functionality")
def test_successful_login():
    with allure.step("Enter username and password"):
        username = "user"
        password = "password"
    with allure.step("Click login button"):
        assert username == "user" and password == "password" # Simulate a successful login
    allure.attach("Login successful", name="Login Status", attachment_type=allure.attachment_type.TEXT)

@allure.feature("Authentication")
@allure.story("Login Functionality")
def test_failed_login():
    with allure.step("Enter incorrect credentials"):
        username = "wrong_user"
        password = "wrong_password"
    with allure.step("Click login button"):
        with pytest.raises(AssertionError): # Simulate a failed login
            assert username == "user"
    allure.attach("Login failed", name="Login Status", attachment_type=allure.attachment_type.TEXT)