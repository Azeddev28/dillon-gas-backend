from django.urls import path

from rest_framework.routers import SimpleRouter

from apis.transactions.bindings import transaction_viewset

router = SimpleRouter()
router.register('', transaction_viewset, basename='transaction')

urlpatterns = []
urlpatterns += router.urls
