from django.urls import path

from apis.notifications.bindings import notification_consumer_websocket


websocket_urlpatterns = [
    path('ws/notifications/<str:room_name>', notification_consumer_websocket)
]
