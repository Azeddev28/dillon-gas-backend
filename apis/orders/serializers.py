from django.contrib.auth import get_user_model
from django.db import transaction as db_transaction

from rest_framework import serializers

from apis.delivery_management.models import DeliveryInfo
from apis.orders.utils.validation_messages import OUT_OF_STOCK_MESSAGE
from apis.orders.serializer_fields.payment_status import PaymentStatusField
from apis.orders.serializer_fields.order_status import OrderStatusField
from apis.orders.serializer_fields.payment_method import PaymentMethodField
from apis.stations.models import StationInventoryItem
from apis.orders.models import Order, OrderItem
from apis.transactions.models import Transaction
from apis.orders.choices import OrderStatus

User = get_user_model()


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='uuid', queryset=StationInventoryItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['item', 'uuid', 'quantity']
        extra_kwargs = {'quantity': {'required': True}}


class TransactionBriefInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['reference',]


class DeliveryAgentOrderUpdateSerializer(serializers.ModelSerializer):
    order_status = OrderStatusField(source='*', required=False)

    class Meta:
        model = Order
        exclude = ['id', 'is_active', 'station']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(), 
        queryset=User.objects.all(),
        slug_field='email'
    )
    order_items = OrderItemSerializer(many=True)
    order_status = OrderStatusField(source='*', required=False)
    payment_status = PaymentStatusField(source='*', required=False)
    payment_method = PaymentMethodField(source='*')
    transaction = TransactionBriefInfoSerializer(many=False, required=False)

    class Meta:
        model = Order
        exclude = ['id', 'is_active', 'station']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['transaction'] = response.get('transaction').get('reference')
        return response

    def _create_or_update_order_items(self, order_items_data, order):
        order_items = []
        for order_item_data in order_items_data:
            try:
                item = order_item_data.pop('item')
                order_item, created = OrderItem.objects.update_or_create(
                    item=item,
                    order=order,
                    defaults={
                        **order_item_data
                    }
                )
                order_items.append(order_item)
            except Exception as e:
                pass

        return order_items

    def _create_transaction(self, amount, user):
        transaction = Transaction.objects.create(
            amount=amount,
            user=user
        )
        return transaction

    def validate(self, attrs):
        attrs = super().validate(attrs)
        order_items = attrs.get('order_items')
        if order_items:
            out_of_stock_items = OrderItem.check_inventory(order_items)
            if out_of_stock_items:
                raise serializers.ValidationError(detail={
                    'message': OUT_OF_STOCK_MESSAGE,
                    'out_of_stock_items': [out_of_stock_items]
                })

        customer = attrs.get('customer')
        if customer:
            customer_address = customer.selected_address
            if not customer_address:
                raise serializers.ValidationError('Customer has not selected address')

            delivery_info = DeliveryInfo.objects.filter(
                city__name__icontains=customer_address.city,
                state__name__icontains=customer_address.state
            ).first()

            if not delivery_info:
                raise serializers.ValidationError('Delivery for this area not supported')

            attrs['delivery_charges'] = delivery_info.delivery_cost

        return attrs

    @db_transaction.atomic
    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        order_items = self._create_or_update_order_items(order_items_data, order)
        base_price = sum([(order_item.item.price * order_item.quantity) for order_item in order_items])
        order.base_price = base_price
        order.total_price = base_price + order.delivery_charges
        order.order_status = OrderStatus.PROCESSING
        order.transaction = self._create_transaction(order.total_price, validated_data.get('customer'))
        OrderItem.deduct_inventory(order_items)
        order.save()
        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items', None)
        order = super().update(instance, validated_data)
        if order_items_data:
            order_items = self._create_or_update_order_items(order_items_data, order)
            base_price = sum([(order_item.item.price * order_item.quantity) for order_item in order_items])
            order.base_price = base_price
            order.total_price = base_price + order.delivery_charges
            order.save()
        return order


class OrderStatusSerializer(serializers.ModelSerializer):
    order_status = OrderStatusField(source='*', required=False)
    class Meta:
        model = Order
        fields = ['order_status',]
