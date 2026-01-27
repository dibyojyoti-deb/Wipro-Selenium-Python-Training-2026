import pytest

@pytest.fixture()
def setup_teardown():
    print("setup")
    yield
    print("Teardown")


def test_example(setup_teardown):
    print("Test 1 running")

def test_example1(setup_teardown):
    print("Test 2 running")