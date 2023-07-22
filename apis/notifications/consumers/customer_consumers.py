import json
import logging

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
logger = logging.getLogger('daphne')


class CustomerNotificationConsumer(WebsocketConsumer):
    def connect(self):
        if self.scope.get('user').is_anonymous:
            self.close()
            return

        user_uuid = self.scope.get('user').uuid
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'notification_{self.room_name}_{user_uuid}'
        logger.info(self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def send_notification(self, event):
        data = event.get('data')

        self.send(text_data=json.dumps(data))

    def receive(self, text_data):
        pass
