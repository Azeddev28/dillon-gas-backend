from rest_framework.generics import ListAPIView

from apis.inventory.models import Category
from apis.inventory.serializers.category import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
