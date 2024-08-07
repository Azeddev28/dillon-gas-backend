from django.urls import path

from apis.third_party_services.flutterwave.bindings import payment_webhook_view


urlpatterns = [
    path('virtual-account-payment-webhook/', payment_webhook_view, name='payment-webhook')
]
