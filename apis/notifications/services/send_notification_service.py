from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class FileGenerationNotificationService:
    NOTIFICATION_TYPE = 'send_notification'

    def __init__(self, file_url, file_instance):
        self.channel_layer = get_channel_layer()
        self.file_url = file_url
        self.file_instance = file_instance

    def get_room_group_name(self):
        return f'notification_report_status_{self.file_instance.user.uuid}'

    def get_data_for_notification(self):
        data = {
            'message': 'Your file is ready to download',
            'file_url': self.file_url,
            'uuid': str(self.file_instance.uuid),
            'file_name': self.file_instance.report_name
        }
        return data

    def send_notification(self):
        async_to_sync(self.channel_layer.group_send)(
            self.get_room_group_name(),
            {
                'type': self.NOTIFICATION_TYPE,
                'data': self.get_data_for_notification()
            }
        )
