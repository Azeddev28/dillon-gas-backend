from rest_framework import serializers
from cities_light.models import City, Region

from apis.delivery_management.models import DeliveryInfo


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ['id', 'created_at', 'updated_at', 'is_active']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', ]


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', ]
