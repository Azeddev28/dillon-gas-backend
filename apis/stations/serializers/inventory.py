from rest_framework import serializers

from apis.stations.models import StationInventory


class InventoryListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    def get_name(self, instance):
        return instance.item.name

    def get_category(self, instance):
        return instance.item.category.name

    class Meta:
        model = StationInventory
        fields = ['name', 'uuid', 'price', 'category']


class InventoryDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_description(self, instance):
        return instance.item.description

    def get_name(self, instance):
        return instance.item.name

    def get_category(self, instance):
        return instance.item.category.name

    class Meta:
        model = StationInventory
        fields = ['name', 'uuid', 'price', 'category', 'description']
