# tests/test_math_utils.py

from exercise_project.test_math_utils import multiply, divide
import pytest

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5
    # now add more test case: (7,9), (2,4), (4,1)
    # ADD CODE HERE


    # END CODE HERE

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    # Test division by zero
    with pytest.raises(ValueError):
        divide(5, 0)
    # now add more test case: (7,2), (2,4), (4,1), (7,0)
    # ADD CODE HERE


    # END CODE HERE
    

