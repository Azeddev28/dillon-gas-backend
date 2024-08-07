from django.db.models import Avg

from rest_framework import serializers

from apis.ratings.models import StarRating
from apis.stations.models import StationInventoryItem


class InventoryListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    average_star_rating = serializers.SerializerMethodField()
    item_uuid = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()

    def get_image(self, instance):
        if getattr(instance.item, 'image'):
            return instance.item.image.url

    def get_item_uuid(self, instance):
        return instance.uuid

    def get_average_star_rating(self, instance):
        return StarRating.objects.filter(item__id=instance.item.id).aggregate(Avg('star_count')).get('star_count__avg')

    def get_name(self, instance):
        return instance.item.name

    def get_category(self, instance):
        return instance.item.category.name

    def get_description(self, instance):
        return instance.item.description

    def get_weight(self, instance):
        return instance.item.weight

    class Meta:
        model = StationInventoryItem
        fields = ['name', 'item_uuid', 'price',
                  'category', 'description', 'average_star_rating', 'image',
                  'weight', 'quantity']


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
        model = StationInventoryItem
        fields = ['name', 'uuid', 'price', 'category', 'description']
