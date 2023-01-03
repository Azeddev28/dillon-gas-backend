from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apis.notifications.notification_codes import RECORD_LOCATION

from apis.orders.serializers import OrderSerializer
from apis.users.utils.choices import ROLES

User = get_user_model()

class OrderAssignmentNotificationService:
    NOTIFICATION_TYPE = 'send_notification'
    BROADCAST_NOTIFICATION_TYPE = 'broadcast_all_agents'

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

    def send_notification(self, group_name):
        '''Send notification for broadcast for delivery agents'''
        async_to_sync(self.channel_layer.group_send)(
            group_name,
            {
                'type': self.BROADCAST_NOTIFICATION_TYPE,
                'data': {
                    'code': RECORD_LOCATION,
                    'message': 'Record Location'
                }
            }
        )

    def broadcast_all_agents_about_order(self):
        delivery_agent_uuids = User.objects.filter(role=ROLES.delivery_agent).values_list('uuid', flat=True)
        for agent_uuid in delivery_agent_uuids:
            group_name = f'notification_rider_{agent_uuid}'
            self.send_notification(group_name)
