import pytest
from bank import BankAccount

@pytest.fixture
def account_with_teardown():
    print("\n[setup]")
    acc = BankAccount(100)
    yield acc
    print("\n[teardown]")

def test_deposit_with_teardown(account_with_teardown):
    account_with_teardown.deposit(50)
    assert account_with_teardown.balance == 150

def test_withdraw_with_teardown(account_with_teardown):
    account_with_teardown.withdraw(30)
    assert account_with_teardown.balance == 70