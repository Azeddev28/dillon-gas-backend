class TransactionStatusChoices:
    PENDING = 0
    FAILED = 1
    COMPLETED = 2

    CHOICES = (
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
        (COMPLETED, 'COMPLETED'),
    )


class WalletTransactionTypeChoices:
    DEPOSIT = 0
    WITHDRAW = 1

    CHOICES = (
        (DEPOSIT, 'Deposit'),
        (WITHDRAW, 'Withdraw'),
    )
