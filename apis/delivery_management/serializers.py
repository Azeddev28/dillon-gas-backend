from rest_framework import serializers
from cities_light.models import City, Region

from apis.delivery_management.models import DeliveryInfo
from apis.users.serializers.customer import CustomerAddressSerializer


class DeliveryInfoSerializer(serializers.ModelSerializer):
    customer_address = serializers.SerializerMethodField()

    def get_customer_address(self, instance):
        selected_address = self.context.get('request').user.selected_address
        if not selected_address:
            return

        customer_address_serializer = CustomerAddressSerializer(selected_address)
        return customer_address_serializer.data

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
