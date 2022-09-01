from django.shortcuts import get_object_or_404

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from apis.delivery_management.models import DeliveryInfo
from apis.delivery_management.serializers import DeliveryInfoSerializer


class DeliveryInfoRetreieveView(RetrieveModelMixin, GenericAPIView):
    serializer_class = DeliveryInfoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        customer_address = self.request.user.user_addresses.filter(selected=True).first()
        if not customer_address:
            raise ValidationError("User has no selected address")

        delivery_info = get_object_or_404(
            DeliveryInfo,
            state__name__icontains=customer_address.state,
            city__name__icontains=customer_address.city
        )
        return delivery_info

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)
