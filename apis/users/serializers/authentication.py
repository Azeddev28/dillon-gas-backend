from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apis.users.utils.messages import (INVALID_LOGIN_MESSAGE,
                                       NO_LOGIN_PARAMS_ENTERETD_MESSAGE)


class DGAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                raise serializers.ValidationError(
                    INVALID_LOGIN_MESSAGE, code='authorization')
        else:
            raise serializers.ValidationError(
                NO_LOGIN_PARAMS_ENTERETD_MESSAGE, code='authorization')

        attrs['user'] = user
        return attrs
