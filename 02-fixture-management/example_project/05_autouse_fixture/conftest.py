import pytest

# Fixture with autouse=True
@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("\n[Setup] Preparing test environment...")
    yield
    print("[Teardown] Cleaning up test environment...")