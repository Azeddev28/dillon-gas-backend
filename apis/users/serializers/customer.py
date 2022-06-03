from django.contrib.auth import get_user_model

from rest_framework import serializers

from apis.users.models import CustomerAddress

User = get_user_model()


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomerAddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            default=serializers.CurrentUserDefault(),
            queryset=User.objects.all(),
            write_only=True
        )

    class Meta:
        model = CustomerAddress
        exclude = ['id', 'created_at', 'updated_at', 'is_active']
