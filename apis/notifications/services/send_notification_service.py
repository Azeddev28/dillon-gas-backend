from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from apis.orders.serializers import OrderSerializer


class OrderAssignmentNotificationService:
    NOTIFICATION_TYPE = 'send_notification'

    def __init__(self, user_uuid, order):
        self.channel_layer = get_channel_layer()
        self.user_uuid = user_uuid
        self.order = order

    def get_room_group_name(self):
        return f'notification_rider_{self.user_uuid}'

    def get_data_for_notification(self):
        order_serializer = OrderSerializer(self.order)
        data = {
            'message': 'Your got an order',
            'order_info': order_serializer.data
        }
        return data

    def send_order_assignment_notification(self):
        async_to_sync(self.channel_layer.group_send)(
            self.get_room_group_name(),
            {
                'type': self.NOTIFICATION_TYPE,
                'data': self.get_data_for_notification()
            }
        )
