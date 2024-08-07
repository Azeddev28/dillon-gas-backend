from apis.orders.choices import OrderStatus, PaymentStatus


NON_EDITABLE_ORDER_STATUS = [OrderStatus.CANCELLED, OrderStatus.COMPLETED]
NON_EDITABLE_PAYMENT_STATUS = [PaymentStatus.COMPLETED, PaymentStatus.FAILED]
