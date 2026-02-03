import pytest
import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"


def test_addition():
    assert add(2, 3) == 5

def test_subtraction_with_message():
    assert subtract(5, 3) == 2, "Subtraction result is incorrect"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.mark.smoke
def test_smoke_multiply():
    assert multiply(3, 4) == 12

@pytest.mark.regression
def test_regression_add():
    assert add(10, 20) == 30

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment_feature():
    assert True

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only_feature():
    assert True


@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert 2 * 2 == 5


def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"

def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"