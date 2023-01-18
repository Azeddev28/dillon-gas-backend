import logging
from django.dispatch import receiver
from django.db.models.signals import post_save

from apis.delivery_management.models import OrderDelivery
from apis.notifications.services.send_notification_service import OrderAssignmentNotificationService

logger = logging.getLogger('daphne')


def find_closest_agent(customer):
    from apis.users.models import DeliveryAgent
    delivery_agents = DeliveryAgent.objects.filter(marked_location=True)
    import math
    import geopy.distance
    closest_distance = math.inf
    closest_agent = None
    customer_latitude = customer.selected_address.latitude
    customer_longitude = customer.selected_address.longitude
    customer_cors = (customer_latitude, customer_longitude)
    logger.info(f'here {customer_cors}')
    logger.info(f'coujnt {delivery_agents.count()}')
    closest_agent_distance = None
    for agent in delivery_agents:
        # find the closest one
        driver_cors = (agent.latitude, agent.longitude)
        logger.info(f'deliver {driver_cors}')
        agent_distance = geopy.distance.geodesic(driver_cors, customer_cors)
        if agent_distance < closest_distance:
            closest_distance = agent_distance
            closest_agent = agent
    
    # found the closest agent
    logger.info("Closest Agent Found")
    return closest_agent


@receiver(post_save, sender=OrderDelivery)
def order_assignment_to_agent(sender, instance, **kwargs):
    user_uuid = instance.delivery_agent.uuid
    order_items = instance.order.order_items.all()
    order_items = [
        {
            'item_name': order_item.item.item.name,
            'price': order_item.item.price,
            'quantity': order_item.quantity,
            'image_url': order_item.item.item.image.url,
        }
        for order_item in order_items
    ]
    order_notification_service = OrderAssignmentNotificationService(user_uuid, instance.order, order_items)
    order_notification_service.send_order_assignment_notification()
