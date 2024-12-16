import pytest

@pytest.fixture(scope="package")
def fixture_package():
    print("Setting up package")
    yield
    print("Tearing down package")

@pytest.fixture(scope="module")
def fixture_module():
    print("Setting up module")
    yield
    print("Tearing down module")

@pytest.fixture(scope="function")
def fixture_function():
    print("Setting up function")
    yield
    #print("Tearing down function")