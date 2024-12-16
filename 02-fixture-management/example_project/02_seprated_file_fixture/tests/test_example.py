from fixtures.example_fixture import sample_data

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