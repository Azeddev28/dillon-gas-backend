from django.apps import AppConfig


class DeliveryManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis.delivery_management'

    def ready(self):
        from apis.orders import signals
