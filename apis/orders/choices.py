PAYMENT_STATUS_CHOICES = (
    ('none', 'None'),
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed')
)

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ('returned', 'Returned'),
    ('dispatched', 'Dispatched')
)

DISCOUNT_TYPE_CHOICES = (
    ('NGN', 'NGN'),
    ('percentage', 'PERCENTAGE')
)

PAYMENT_CHOICES = (
    ('cash_on_delivery', 'Cash on Delivery'),
    ('card', 'Card'),
    ('cash_in_hand', 'Cash in Hand')
)

ORDER_TYPE_CHOICES = (
    ('home_delivery', 'Home Delivery'),
    ('pickup', 'Pickup'),
    ('in_shop', 'In Shop'),
    ('payment_by_phone', 'Payment By Phone')
)
