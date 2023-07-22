from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apis.notifications.notification_codes import RECORD_LOCATION

from apis.users.utils.choices import ROLES
import logging
logger = logging.getLogger('daphne')

User = get_user_model()

class OrderAssignmentNotificationService:
    NOTIFICATION_TYPE = 'send_notification'
    BROADCAST_NOTIFICATION_TYPE = 'broadcast_all_agents'

    def __init__(self, user_uuid, order, order_items=None):
        self.channel_layer = get_channel_layer()
        self.user_uuid = user_uuid
        self.order = order
        if order_items:
            self.order_items = order_items

    def get_room_group_name(self):
        return f'notification_rider_{self.user_uuid}'

    def get_data_for_notification(self):
        import json
        logger.error(self.order.uuid)
        logger.error(self.order.customer.consumer_coordinates)
        data = {
            'code': 'RECEIVED_ORDER',
            'message': 'Your got an order',
            'order_info': {
                'order_uuid': str(self.order.uuid),
                'customer_name': self.order.customer.full_name,
                'drop_location': str(self.order.customer.selected_address),
                'total_price': self.order.total_price,
                'consumer_coordinates': json.dumps(self.order.customer.consumer_coordinates),
                'order_items': json.dumps(self.order_items)
            }
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
        order_city = self.order.customer.selected_address.city
        print(order_city)
        delivery_agent_uuids = User.objects.filter(
            role=ROLES[0][0], delivery_agent__assigned_city__name=order_city
        ).values_list('uuid', flat=True)
        print(delivery_agent_uuids)
        for agent_uuid in delivery_agent_uuids:
            print(agent_uuid)
            logger.error(agent_uuid)
            group_name = f'notification_rider_{agent_uuid}'
            self.send_notification(group_name)
