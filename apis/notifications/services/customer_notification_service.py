from django.contrib.auth import get_user_model

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apis.notifications.notification_codes import RECORD_LOCATION
from apis.orders.choices import OrderStatus

from apis.users.utils.choices import ROLES
import logging
logger = logging.getLogger('daphne')

User = get_user_model()

class CustomerNotificationService:
    NOTIFICATION_TYPE = 'send_notification'

    def __init__(self, customer, order, delivery_agent=None):
        self.channel_layer = get_channel_layer()
        self.order = order
        self.customer = customer
        self.agent_user = delivery_agent
        logger.info("YOU ARE GREAT")

    def get_room_group_name(self):
        return f'notification_user_{self.customer.uuid}'

    def get_order_delivered_notification(self):
        data = {
            'code': 'ORDER_DELIVERED',
            'message': 'Your order has been delieverd!',
        }
        return data

    def get_data_for_notification(self):
        import json
        data = {
            'code': 'ORDER_PICKED_UP',
            'message': 'Your got an order',
            'order_info': {
                'delivery_agent_name': self.agent_user.full_name,
                'customer_address': str(self.customer.selected_address),
                'customer_coordinates': {
                    'longitude': self.customer.selected_address.longitude,
                    'latitude': self.customer.selected_address.latitude
                },
                'agent_coordinates': {
                    'longitude': self.agent_user.delivery_agent.longitude,
                    'latitude': self.agent_user.delivery_agent.latitude
                }
            }
        }
        return data

    def send_notification(self):
        group_name = self.get_room_group_name()
        logger.info(str(group_name))
        logger.info("HESS")
        logger.error(self.order.order_status)
        if self.order.order_status == OrderStatus.COMPLETED:
            data = self.get_order_delivered_notification()
        else:
            data = self.get_data_for_notification()
        async_to_sync(self.channel_layer.group_send)(
            group_name,
            {
                'type': self.NOTIFICATION_TYPE,
                'data': data
            }
        )
