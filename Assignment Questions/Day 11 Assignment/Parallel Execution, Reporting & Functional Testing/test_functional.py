import pytest
import time

# Functional test with dependencies
@pytest.fixture
def user_session():
    # Setup: Log in
    session = {"user": "admin", "token": "12345"}
    yield session
    # Teardown: Log out
    session.clear()

def test_user_login_flow(user_session):
    """E2E: Verify user can log in and access profile."""
    assert user_session["user"] == "admin"
    time.sleep(1)  # Simulating network latency

def test_checkout_process(user_session):
    """E2E: Verify authenticated user can complete a purchase."""
    cart = ["item1", "item2"]
    order_status = "Success" if user_session["token"] else "Failed"
    assert order_status == "Success"
    time.sleep(1)

@pytest.mark.parametrize("item", ["phone", "laptop", "tablet"])
def test_search_functionality(item):
    """Functional: Verify search works for multiple product categories."""
    search_results = [item]
    assert item in search_results
    time.sleep(1)