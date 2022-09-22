from django.db.models import Case, When

from rest_framework.generics import ListAPIView

from apis.inventory.models import Category
from apis.inventory.serializers.category import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by(
        Case(When(name="All", then=0), default=1)
    )
