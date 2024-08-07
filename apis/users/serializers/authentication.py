from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_user_token')

    class Meta:
        model = User

    def get_user_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key
