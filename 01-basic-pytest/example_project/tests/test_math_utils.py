# Tests for math_utils module
from example_project.math_utils import add, subtract

def test_add():
    """Tests the add function with various inputs."""
    # Positive numbers
    assert add(2, 3) == 5
    # Adding a negative number
    assert add(-1, 1) == 0
    # Adding zero
    assert add(0, 0) == 0

def test_subtract():
    """Tests the subtract function with various inputs."""
    # Subtracting smaller from larger
    assert subtract(5, 3) == 2
    # Subtracting larger from smaller
    assert subtract(3, 5) == -2
    # Subtracting zero
    assert subtract(0, 0) == 0
