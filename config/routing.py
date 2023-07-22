from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from config.middleware.websock_authentication import JWTAuthMiddleware
from apis.notifications.routing import websocket_urlpatterns as notification_websocket_urlpatterns


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': JWTAuthMiddleware(
        URLRouter(
            notification_websocket_urlpatterns
        )
    )
})
