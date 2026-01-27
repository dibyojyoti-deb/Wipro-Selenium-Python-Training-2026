import pytest
from calculator import multiply, divide


def test_multiplication_large(large_numbers):
    a, b = large_numbers
    assert multiply(a, b) == 2000


def test_division_large(large_numbers):
    a, b = large_numbers
    assert divide(a, b) == 5


def test_division_by_zero(numbers):
    a, _ = numbers
    with pytest.raises(ZeroDivisionError):
        divide(a, 0)
