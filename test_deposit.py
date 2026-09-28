import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit_positive(account):
    assert account.deposit(50) == 150

def test_deposit_zero(account):
    assert account.deposit(0) == 100
