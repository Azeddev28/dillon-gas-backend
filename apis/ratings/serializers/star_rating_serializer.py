from django.db.models import Avg

from rest_framework import serializers

from apis.ratings.models import StarRating


class StarRatingSerializer(serializers.ModelSerializer):
    average_star_rating = serializers.SerializerMethodField()

    def get_average_star_rating(self, instance):
        return StarRating.objects.filter(item=instance.item).aggregate(Avg('star_count')).get('star_count__avg')

    class Meta:
        model = StarRating
        fields = ['average_star_rating']
