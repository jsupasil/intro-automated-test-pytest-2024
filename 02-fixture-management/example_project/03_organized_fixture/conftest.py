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