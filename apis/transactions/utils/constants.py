from apis.transactions.choices import TransactionStatus


NON_EDITABLE_TRANSACTION_STATUS = [
    TransactionStatus.COMPLETED, 
    TransactionStatus.FAILED
]
