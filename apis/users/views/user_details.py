from rest_framework.generics import RetrieveUpdateAPIView

from apis.users.serializers.customer import CustomerDetailsSerializer


class CustomerDetailsRetrieveAPIView(RetrieveUpdateAPIView):
    serializer_class = CustomerDetailsSerializer

    def get_object(self):
        return self.request.user
