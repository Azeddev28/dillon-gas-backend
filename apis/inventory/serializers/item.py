from rest_framework import serializers

from apis.inventory.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'uuid']
