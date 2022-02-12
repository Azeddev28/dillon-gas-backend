from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

User = get_user_model()


class ResendEmailSerializer(serializers.Serializer):
    """Serializer to send verification email"""
    email = serializers.EmailField()

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        user = None
        try:
            user = User.objects.get(email=attrs.get('email'))
        except User.DoesNotExist:
            msg = 'Invalid Email!'
            raise serializers.ValidationError(msg, code='verification')

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
            msg = 'Invalid Email!'
            raise serializers.ValidationError(msg, code='verification')

        request = self.context['request']
        user_email = request.session['email']
        user_verification_code = request.session['verification_code']

        if user_email != attrs.get('email') or user_verification_code != attrs.get('verification_code'):
            msg = 'Invalid code entered!'
            raise serializers.ValidationError(msg, code='verification')

        validated_data['user'] = user
        return validated_data
