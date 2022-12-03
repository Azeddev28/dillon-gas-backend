from django.dispatch import receiver
from django.db.models.signals import post_save

from apis.delivery_management.models import OrderDelivery
from apis.notifications.services.send_notification_service import OrderAssignmentNotificationService


@receiver(post_save, sender=OrderDelivery)
def order_assignment_to_agent(sender, instance, **kwargs):
    user_uuid = instance.order.customer.uuid
    order_notification_service = OrderAssignmentNotificationService(user_uuid)
    order_notification_service.send_order_assignment_notification()
