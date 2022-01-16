import firebase_admin
from firebase_admin import messaging

from app.models.Notification import Notification

path_to_firebase_credentials_file = "firebase-project-credentials.json"


class NotificationService:
    def __init__(self):
        if not firebase_admin._apps:
            firebase_cred = firebase_admin.credentials.Certificate(path_to_firebase_credentials_file)
            firebase_admin.initialize_app(firebase_cred)

    def send_notification(self, notif: Notification):
        message = messaging.Message(
            notification=messaging.Notification(
                title=notif.title,
                body=notif.body
            ),
            topic=notif.topic
        )
        return messaging.send(message)
