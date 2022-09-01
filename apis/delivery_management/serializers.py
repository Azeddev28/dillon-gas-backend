from rest_framework import serializers

from apis.delivery_management.models import DeliveryInfo


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ['id', 'created_at', 'updated_at', 'is_active']
