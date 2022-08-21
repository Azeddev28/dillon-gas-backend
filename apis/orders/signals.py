from django.dispatch import receiver
from django.db.models.signals import pre_save
from apis.orders.choices import OrderStatus

from apis.orders.models import Order
from apis.services.email_service import EmailService
from apis.orders.mappings import order_tracking_template_mapping


# @receiver(post_save, sender=Order)
# def notify_delivery_agents(sender, created, instance, **kwargs):
#     if created:
#         pass


@receiver(pre_save, sender=Order)
def order_tracking(sender, instance, **kwargs):
    if instance.order_status == OrderStatus.PENDING:
        return

    prev_order_status = Order.objects.get(id=instance.id).order_status
    if prev_order_status == instance.order_status:
        return

    template_name = order_tracking_template_mapping.get(instance.order_status)
    email_service = EmailService(
        'Order Tracking',
        [instance.customer.email, ],
        template_name,
        {
            'order': instance,
            'customer_address': instance.customer.user_addresses.filter(selected=True).first()
        }
    )
    email_service.start()
