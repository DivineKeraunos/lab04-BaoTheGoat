import pytest

@pytest.fixture
def setup_teardown():
    print("[setup]")
    yield 
    print("[teardown]")

def test_first(setup_teardown):
    print("Running first test")
    assert True

def test_second(setup_teardown):
    print("Running second test")
    assert True