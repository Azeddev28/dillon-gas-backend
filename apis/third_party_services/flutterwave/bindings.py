from apis.third_party_services.flutterwave.webhooks import VirtualAccountPaymentWebhook


payment_webhook_view = VirtualAccountPaymentWebhook.as_view()
