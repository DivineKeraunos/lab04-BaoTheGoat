def test_funded_account_can_deposit_money(funded_account):
    
    deposit_amount = 200
    expected_balance = 1200

    
    actual_balance = funded_account.deposit(deposit_amount)

    
    assert actual_balance == expected_balance
    assert funded_account.balance == expected_balance


def test_funded_account_can_withdraw_money(funded_account):
    
    withdrawal_amount = 250
    expected_balance = 750

    
    actual_balance = funded_account.withdraw(withdrawal_amount)

    
    assert actual_balance == expected_balance
    assert funded_account.balance == expected_balance