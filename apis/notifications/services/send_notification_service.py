from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class OrderAssignmentNotificationService:
    NOTIFICATION_TYPE = 'send_notification'

    def __init__(self, user_uuid):
        self.channel_layer = get_channel_layer()
        self.user_uuid = user_uuid

    def get_room_group_name(self):
        return f'notification_rider_{self.user_uuid}'

    def get_data_for_notification(self):
        data = {
            'message': 'Your got an order',
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
