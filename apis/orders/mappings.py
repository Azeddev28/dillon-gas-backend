order_tracking_template_mapping = {
    'Processing': 'email_templates/order_confirmation.html',
    'Dispatched': 'email_templates/order_dispatch_confirmation.html',
    'Completed': 'email_templates/order_completion_confirmation.html',
    'Cancelled': 'email_templates/order_completion_confirmation.html',
}

order_subject_mapping = {
    'Processing': 'Order Confirmation',
    'Dispatched': 'Order Dispatch Confirmation',
    'Completed': 'Order Completion',
    'Cancelled': 'Order Cancellation',
}
