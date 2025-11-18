# tests/test_keycloak.py
import requests
import pytest

KEYCLOAK_URL = "http://localhost:8080/auth"  # This will point to the Keycloak running in GitHub Actions
REALM_NAME = "your-realm"  # Replace with your Keycloak realm
CLIENT_ID = "your-client-id"  # Replace with your Keycloak client ID
USERNAME = "testuser"
PASSWORD = "password"
EMAIL = "testuser@example.com"

@pytest.fixture(scope="module")
def create_user():
    """Fixture to create a user in Keycloak."""
    admin_username = "admin"
    admin_password = "admin_password"
    admin_client_id = "admin-cli"

    # Get admin token
    token_response = requests.post(
        f"{KEYCLOAK_URL}/realms/{REALM_NAME}/protocol/openid-connect/token",
        data={
            "client_id": admin_client_id,
            "username": admin_username,
            "password": admin_password,
            "grant_type": "password",
        },
    )
    token = token_response.json()["access_token"]

    # Create user
    create_user_response = requests.post(
        f"{KEYCLOAK_URL}/admin/realms/{REALM_NAME}/users",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={
            "username": USERNAME,
            "enabled": True,
            "email": EMAIL,
            "firstName": "Test",
            "lastName": "User"
        }
    )
    return create_user_response.status_code

def test_user_creation(create_user):
    assert create_user == 201, "User creation failed."

def test_login():
    response = requests.post(
        f"{KEYCLOAK_URL}/realms/{REALM_NAME}/protocol/openid-connect/token",
        data={
            "client_id": CLIENT_ID,
            "username": USERNAME,
            "password": PASSWORD,
            "grant_type": "password",
        },
    )
    assert response.status_code == 200, "Login failed."

def test_logout():
    # You may implement logout test if applicable
    pass