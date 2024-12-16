# Tests for string_utils module
from example_project.string_utils import reverse_string, capitalize_string

def test_reverse_string():
    """Tests the reverse_string function with various inputs."""
    # Normal string
    assert reverse_string("hello") == "olleh"
    # Empty string
    assert reverse_string("") == ""
    # Single character string
    assert reverse_string("a") == "a"

def test_capitalize_string():
    """Tests the capitalize_string function with various inputs."""
    # Normal string
    assert capitalize_string("hello") == "Hello"
    # Another normal string
    assert capitalize_string("python") == "Python"
    # Empty string
    assert capitalize_string("") == ""
