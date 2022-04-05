from rest_framework.generics import RetrieveAPIView

from apis.users.serializers.customer import CustomerDetailsSerializer


class CustomerDetailsRetrieveAPIView(RetrieveAPIView):
    serializer_class = CustomerDetailsSerializer

    def get_object(self):
        return self.request.user
