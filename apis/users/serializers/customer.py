from django.contrib.auth import get_user_model

from rest_framework import serializers

from apis.users.models import CustomerAddress

User = get_user_model()


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class CustomerAddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            default=serializers.CurrentUserDefault(),
            queryset=User.objects.all(),
            write_only=True
        )

    class Meta:
        model = CustomerAddress
        exclude = ['id', 'created_at', 'updated_at', 'is_active']

    def create(self, validated_data):
        user = validated_data.get('user')
        CustomerAddress.objects.filter(user=user).update(selected=False)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        CustomerAddress.objects.filter(user=instance.user).update(selected=False)
        return super().update(instance, validated_data)
