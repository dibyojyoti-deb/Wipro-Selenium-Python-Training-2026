from calculator import add, subtract


# xUnit-style setup / teardown
def setup_module():
    print("\nSetup before module")


def teardown_module():
    print("\nTeardown after module")


def setup_function():
    print("Setup before test function")


def teardown_function():
    print("Teardown after test function")


def test_addition(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_subtraction(numbers):
    a, b = numbers
    assert subtract(a, b) == 5
