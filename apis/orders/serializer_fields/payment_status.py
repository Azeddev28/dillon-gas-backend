from rest_framework import serializers

from apis.orders.choices import PaymentStatus


class PaymentStatusField(serializers.Field):

    def to_representation(self, value):
        return value.get_payment_status_display()

    def to_internal_value(self, data):
        payment_status_value = getattr(PaymentStatus, data)
        return {'payment_status': payment_status_value}
