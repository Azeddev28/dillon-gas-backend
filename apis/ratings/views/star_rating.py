from rest_framework.generics import RetrieveAPIView

from apis.ratings.models import StarRating
from apis.ratings.serializers.star_rating_serializer import StarRatingSerializer


class StarRatingRetrieveAPIView(RetrieveAPIView):
    serializer_class = StarRatingSerializer
    queryset = StarRating.objects.all()
    lookup_field = 'item__uuid'
