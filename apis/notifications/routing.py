from django.urls import path

from apis.notifications.bindings import rider_notification_consumer_websocket, customer_notification_consumer_websocket


websocket_urlpatterns = [
    path('ws/notifications/<str:room_name>', rider_notification_consumer_websocket),
    path('ws/notifications/customers/<str:room_name>', customer_notification_consumer_websocket)
]
