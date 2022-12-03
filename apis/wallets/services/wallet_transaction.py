from apis.transactions.choices import WalletTransactionTypeChoices
from apis.transactions.models import WalletTransaction


class WalletTransactionService:
    def __init__(self, amount, user, transaction_type=WalletTransactionTypeChoices.TOP_UP):
        self.transaction = WalletTransaction(
            amount=amount,
            user=user,
            transaction_type=transaction_type
        )
        self.transaction.save(commit=False)
        
    def validate_charge(self):
        pass

    def top_up(self):
        wallet = self.transaction.user.wallet
        wallet.total_amount += self.transaction.amount
        wallet.save()
    
    def consume_amount(self):
        if self.transaction.amount > wallet.total_amount:
            return False

        wallet = self.transaction.user.wallet
        wallet.total_amount -= self.transaction.amount
        wallet.save()
        return True
