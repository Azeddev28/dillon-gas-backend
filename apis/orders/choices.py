class PaymentStatus:
    PENDING = 1
    COMPLETED = 2
    FAILED = 3
    CHOICES = (
    (PENDING, 'Pending'),
    (COMPLETED, 'Completed'),
    (FAILED, 'Failed')
)

class OrderStatus:
    PENDING = 1
    DELIVERED = 2
    CANCELLED = 3
    RETURNED = 4
    DISPATCHED = 5
    CHOICES = (
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
        (RETURNED, 'Returned'),
        (DISPATCHED, 'Dispatched')
    )

DISCOUNT_TYPE_CHOICES = (
    ('NGN', 'NGN'),
    ('percentage', 'PERCENTAGE')
)

class PaymentMethods:
    PAY_ONLINE = 1
    WALLET = 2

    CHOICES = (
        (PAY_ONLINE, 'Pay Online'),
        (WALLET, 'Wallet')
    )

ORDER_TYPE_CHOICES = (
    ('home_delivery', 'Home Delivery'),
    ('pickup', 'Pickup'),
    ('in_shop', 'In Shop'),
    ('payment_by_phone', 'Payment By Phone')
)
