from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apis.transactions.models import Transaction
from apis.transactions.serializers import TransactionSerializer


class TransactionModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    queryset = Transaction.objects.all()
