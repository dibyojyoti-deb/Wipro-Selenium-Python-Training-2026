import pytest


# Function-scope fixture (default)
@pytest.fixture
def numbers():
    return 10, 5


# Module-scope fixture
@pytest.fixture(scope="module")
def large_numbers():
    return 100, 20
