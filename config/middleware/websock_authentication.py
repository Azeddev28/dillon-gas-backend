from urllib.parse import parse_qs
from django.db import close_old_connections
from django.conf import settings
from django.contrib.auth import get_user_model
from django_cognito_jwt.validator import TokenError, TokenValidator
from django.contrib.auth.models import AnonymousUser

from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async


User = get_user_model()


@database_sync_to_async
def get_user(user_uuid):
    try:
        return User.objects.get(uuid=user_uuid)
    except User.DoesNotExist:
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner
        self.token_validator = TokenValidator(
            settings.COGNITO_AWS_REGION,
            settings.COGNITO_USER_POOL,
            settings.COGNITO_AUDIENCE,
        )

    async def __call__(self, scope, receive, send):
        close_old_connections()

        try:
            token_key = parse_qs(scope['query_string'].decode('utf-8'))['token'][0].split()[1]
            jwt_payload = self.token_validator.validate(token_key)
        except (TokenError, Exception) as e:
            raise ValueError(
                f'Exception occurred while authenticating Websocket request {e}')

        user = await get_user(jwt_payload['sub'])
        scope['user'] = user
        return await super().__call__(scope, receive, send)


def JWTAuthMiddlewareStack(inner): 
    return JWTAuthMiddleware(AuthMiddlewareStack(inner))
