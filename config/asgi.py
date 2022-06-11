"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import django

from config.setup_environment import setup_environment
from channels.routing import get_default_application

setup_environment()
django.setup()


application = get_default_application()
