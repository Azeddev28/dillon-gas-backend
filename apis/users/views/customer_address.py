from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apis.users.models import CustomerAddress
from apis.users.serializers.customer import CustomerAddressSerializer


class CustomerAddressModelViewset(ModelViewSet):
    serializer_class = CustomerAddressSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'uuid'
    
    def get_queryset(self):
        user = self.request.user
        return CustomerAddress.objects.filter(user=user)
