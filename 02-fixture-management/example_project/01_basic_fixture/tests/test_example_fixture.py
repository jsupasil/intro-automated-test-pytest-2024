import pytest

# Define a simple fixture inside the test file
@pytest.fixture
def sample_data():
    """Fixture to provide sample data for the tests."""
    print("\nSetting up sample data")
    data = {"key1": "value1", "key2": "value2"}  # Sample data
    yield data  # This is the value that will be used in tests
    print("\nTearing down sample data")
    # Add code here to clean up if necessary (not needed in this example)

# Test case 1: Using the fixture
def test_example_1(sample_data):
    """Test that checks the sample data."""
    print("Running test_example_1")
    assert sample_data["key1"] == "value1"
    assert sample_data["key2"] == "value2"

# Test case 2: Using the fixture
def test_example_2(sample_data):
    """Test that checks the sample data again."""
    print("Running test_example_2")
    assert "key1" in sample_data
    assert "key2" in sample_data

