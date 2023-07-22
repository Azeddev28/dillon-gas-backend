from django.urls import path
from apis.orders.views.orders import DeliveryAgentOrderUpdate, OrderViewSet, FetchOrderStatusAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', OrderViewSet, basename='orders')


urlpatterns = [
    path('order-status/<uuid:uuid>/', FetchOrderStatusAPIView.as_view(), name='order-status'),
    path('agent-order-update/', DeliveryAgentOrderUpdate.as_view(), name='agent-order-update'),
    *router.urls
]
