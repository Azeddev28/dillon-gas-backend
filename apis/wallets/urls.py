from django.urls import path

from rest_framework.routers import SimpleRouter

from apis.wallets.bindings import virtual_account_retrieve_api_view

router = SimpleRouter()
# router.register('payment-card', PaymentCardModelViewset, basename='orders')


urlpatterns = [
    path('virtual-account/', virtual_account_retrieve_api_view, name='virtual-account')
    # *router.urls
]
