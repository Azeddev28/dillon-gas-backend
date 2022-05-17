from django.urls import path
from apis.orders.views.orders import OrderViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', OrderViewSet, basename='orders')


urlpatterns = [
    *router.urls
]
