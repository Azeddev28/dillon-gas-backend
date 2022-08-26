from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from apis.orders.choices import OrderStatus
from apis.orders.models import Order
from apis.services.email_service import EmailService
from apis.orders.mappings import order_tracking_template_mapping

User = get_user_model()

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

    template_name = order_tracking_template_mapping.get(instance.get_order_status_display())
    if not template_name:
        return

    try:
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
    except Exception as e:
        pass


@receiver(post_save, sender=Order)
def order_placement_tracking(sender, instance, **kwargs):
    if instance.order_status == OrderStatus.PENDING:
        return

    if instance != OrderStatus.PROCESSING:
        return

    template_name = 'email_templates/admin_emails/order_placement_email.html'

    receipient_emails = User.objects.filter(email_support=True).values_list('email', flat=True)
    try:
        email_service = EmailService(
            'Order Placement',
            receipient_emails,
            template_name,
            {
                'order_edit_url': f"{Site.objects.get_current().domain}{reverse('admin:orders_order_change', args=(instance.id,))}",
            }
        )
        email_service.start()
    except Exception as e:
        pass
