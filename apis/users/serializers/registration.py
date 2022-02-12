from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from apis.users.models import UserDevice

User = get_user_model()


def _create_device_info(user, device):
    UserDevice.objects.create(user=user, device_id=device.get('device_id'))


def _create_user(user_info):
    user_info.pop('password', None)
    user_info.pop('password2', None)
    user = User.objects.create(**user_info)
    return user


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ['device_id']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for User Registration"""

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    device = DeviceSerializer()
    is_active = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'role', 'password2', 'password',
                  'created_at', 'device', 'phone_number',
                  'is_active']
        write_only_fields = ['password', 'password2']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            msg = 'passwords must match'
            raise serializers.ValidationError({'password': msg})

        return validated_data

    @transaction.atomic
    def create(self, validated_data):
        device = validated_data.pop('device', None)
        user = _create_user(validated_data)
        _create_device_info(user, device)
        return user
