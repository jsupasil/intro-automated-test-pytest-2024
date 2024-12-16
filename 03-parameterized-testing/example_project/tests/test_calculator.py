import pytest
from example_project.calculator import add

# Parameterized test for the add function
@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),   # Test case 1
    (0, 0, 0),   # Test case 2
    (-1, 1, 0),  # Test case 3
    (100, 200, 300),  # Test case 4
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
