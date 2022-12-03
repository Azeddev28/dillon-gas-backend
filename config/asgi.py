"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import django

from config.setup_environment import setup_environment
# from channels.routing import get_default_application
from django.core.asgi import get_asgi_application
import os


# setup_environment()
# django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter

from config.middleware.websock_authentication import JWTAuthMiddleware
from apis.notifications.routing import websocket_urlpatterns as notification_websocket_urlpatterns


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': JWTAuthMiddleware(
        URLRouter(
            notification_websocket_urlpatterns
        )
    )
})
