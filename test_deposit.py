import pytest
from bank import BankAccount
@pytest.fixture
def account():
    return BankAccount(100)
def test_deposit_updates_balance(account):
    account.deposit(50)
    assert account.balance == 150
def test_deposit_returns_new_balance(account):
    new_balance = account.deposit(25)
    assert new_balance == 125
    assert account.balance == 125