from apis.orders.choices import OrderStatus


order_tracking_template_mapping = {
    OrderStatus.PROCESSING: 'email_templates/order_confirmation.html',
    OrderStatus.DISPATCHED: 'email_templates/order_dispatch_confirmation.html',
    OrderStatus.COMPLETED: 'email_templates/order_completion_confirmation.html',
}
