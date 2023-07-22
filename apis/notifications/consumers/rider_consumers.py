import json
import logging

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
logger = logging.getLogger('daphne')


class RiderNotificationConsumer(WebsocketConsumer):
    def connect(self):
        if self.scope.get('user').is_anonymous:
            self.close()
            return

        user_uuid = self.scope.get('user').uuid
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'notification_{self.room_name}_{user_uuid}'

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

    def broadcast_all_agents(self, event):
        data = event.get('data')

        self.send(text_data=json.dumps(data))

    def receive(self, text_data):
        import json
        text_data = json.loads(text_data)
        logger.error(self.scope.get('user'))
        logger.error(self.scope.get('user').uuid)
        delivery_agent = self.scope.get('user').delivery_agent
        delivery_agent.latitude = text_data.get('latitude')
        delivery_agent.longitude = text_data.get('longitude')
        delivery_agent.marked_location = True
        logger.error(delivery_agent.marked_location, "HER")
        delivery_agent.save()
