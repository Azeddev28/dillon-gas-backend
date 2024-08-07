from rest_framework import serializers

from apis.orders.choices import PaymentMethods


class PaymentMethodField(serializers.Field):

    def to_representation(self, value):
        return value.get_payment_method_display()

    def to_internal_value(self, data):
        payment_method_value = getattr(PaymentMethods, data)
        return {'payment_method': payment_method_value}
