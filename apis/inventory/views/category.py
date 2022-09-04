from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apis.inventory.models import Category
from apis.inventory.serializers.category import CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
