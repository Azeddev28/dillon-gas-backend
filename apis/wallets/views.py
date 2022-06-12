from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apis.wallets.models import PaymentCard
from apis.wallets.serializers import PaymentCardSerializer


class PaymentCardModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = PaymentCardSerializer
    queryset = PaymentCard.objects.all()
