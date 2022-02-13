from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apis.users.services.email_verification import EmailVerificationService
from apis.users.utils.messages import (INVALID_CODE_MESSAGE,
                                       INVALID_EMAIL_MESSAGE,
                                       INVALID_VERIFICATION_REQUEST_MESSAGE)

User = get_user_model()


class ResendEmailSerializer(serializers.Serializer):
    """Serializer to send verification email"""
    email = serializers.EmailField()
    verification_code = serializers.CharField(default=EmailVerificationService.generate_verification_code())

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        user = None
        try:
            user = User.objects.get(email=attrs.get('email'))
        except User.DoesNotExist:
            raise serializers.ValidationError(INVALID_EMAIL_MESSAGE, code='verification')

        validated_data['user'] = user
        return validated_data


class EmailVerificationSerializer(serializers.Serializer):
    """Serializer to verify user email"""
    verification_code = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        user = None
        try:
            user = User.objects.get(email=attrs.get('email'))
        except User.DoesNotExist:
            raise serializers.ValidationError(INVALID_EMAIL_MESSAGE, code='verification')

        request = self.context['request']
        user_email = request.session.get('email')
        user_verification_code = request.session.get('verification_code')
        if not user_email or not user_verification_code:
            raise serializers.ValidationError(INVALID_VERIFICATION_REQUEST_MESSAGE, code='verification')

        if user_email != attrs.get('email') or user_verification_code != attrs.get('verification_code'):
            raise serializers.ValidationError(INVALID_CODE_MESSAGE, code='verification')

        validated_data['user'] = user
        return validated_data
