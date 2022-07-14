from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from apis.users.models import UserDevice
from apis.users.services.email_verification import EmailVerificationService
from apis.users.utils.messages import PASSWORD_MATCH_ERROR_MESSAGE

User = get_user_model()


def _create_device_info(user, device_id):
    UserDevice.objects.create(user=user, device_id=device_id)


def _create_user(validated_data):
    user_info = validated_data.copy()
    user_info.pop('verification_code')
    user_info.pop('password2', None)
    user = User.objects.create(**user_info)
    return user


def _verify_user(user_email, verification_code):
    email_service = EmailVerificationService(
        recipient_email=user_email,
        verification_code=verification_code
    )
    email_service.send_email()


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['device_id']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for User Registration"""
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    device_id = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(default=False)
    verification_code = serializers.CharField(default=EmailVerificationService.generate_verification_code())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'role', 'password', 'created_at', 'device_id',
                  'is_active', 'verification_code', 'phone_number']
        read_only_fields = ['created_at', 'updated_at']

    @transaction.atomic
    def create(self, validated_data):
        device_id = validated_data.pop('device_id', None)
        user = _create_user(validated_data)
        _create_device_info(user, device_id)
        _verify_user(user.email, validated_data.get('verification_code'))
        return user
