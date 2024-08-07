from django.urls import path
from apis.orders.views.orders import OrderViewSet, FetchOrderStatusAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', OrderViewSet, basename='orders')


urlpatterns = [
    path('order-status/<uuid:uuid>/', FetchOrderStatusAPIView.as_view(), name='order-status'),
    *router.urls
]
