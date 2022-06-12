from rest_framework import serializers

from apis.wallets.models import PaymentCard


class PaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCard
        fields = ['card_number', 'cvv', 'expiry_month', 'expiry_year']
