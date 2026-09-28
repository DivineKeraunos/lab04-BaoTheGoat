def test_funded_account_can_deposit_money(funded_account):
    # Arrange
    deposit_amount = 200
    expected_balance = 1200

    # Act
    actual_balance = funded_account.deposit(deposit_amount)

    # Assert
    assert actual_balance == expected_balance
    assert funded_account.balance == expected_balance


def test_funded_account_can_withdraw_money(funded_account):
    # Arrange
    withdrawal_amount = 250
    expected_balance = 750

    # Act
    actual_balance = funded_account.withdraw(withdrawal_amount)

    # Assert
    assert actual_balance == expected_balance
    assert funded_account.balance == expected_balance