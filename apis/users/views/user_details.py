from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apis.users.serializers.customer import CustomerDetailsSerializer


class CustomerDetailsRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = CustomerDetailsSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user
