import pytest
from utilities.math_utils import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_invalid_input():
    with pytest.raises(ValueError):
        add(2, "3")
