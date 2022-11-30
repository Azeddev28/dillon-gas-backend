from urllib.parse import parse_qs
from django.db import close_old_connections
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from rest_framework_simplejwt.authentication import JWTAuthentication

from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async


User = get_user_model()


@database_sync_to_async
def get_user(token_key):
    try:
        token_auth = JWTAuthentication()
        token = token_auth.get_validated_token(token_key)
        user = token_auth.get_user(token)
        return user
    except Exception as e:
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        close_old_connections()

        try:
            token_key = parse_qs(scope['query_string'].decode('utf-8'))['token'][0]
        except Exception as e:
            raise ValueError(
                f'Exception occurred while authenticating Websocket request {e}')

        user = await get_user(token_key)
        scope['user'] = user
        return await super().__call__(scope, receive, send)


def JWTAuthMiddlewareStack(inner):
    return JWTAuthMiddleware(AuthMiddlewareStack(inner))
