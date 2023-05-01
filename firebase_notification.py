import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("../dillon-gas-backend/firebase_creds.json")
firebase_admin.initialize_app(cred)


class FirebasePushNotifications:
    def __init__(self):
        pass
    
    def send_device_notification(self, user, title, notification_body):
        fcm_token = user.device.fcm_token
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=notification_body
            ),
            token=fcm_token
        )

        # Send the message
        response = messaging.send(message)