from django.dispatch import receiver
from django.db.models.signals import post_save

from apis.delivery_management.models import OrderDelivery
from apis.notifications.services.send_notification_service import OrderAssignmentNotificationService
import time

from apis.users.models import DeliveryAgent
import logging
logger = logging.getLogger('daphne')


def find_closest_agent(customer):
    from apis.users.models import DeliveryAgent
    delivery_agents = DeliveryAgent.objects.filter(marked_location=True)
    import math
    import geopy.distance
    closest_distance = math.inf
    closest_agent = None
    customer_lat = '31.582045'
    customer_long = '74.329376'
    customer_cors = (customer_lat, customer_long)
    for agent in delivery_agents:
        # find the closest one
        driver_cors = (agent.latitude, agent.longitude)
        agent_distance = geopy.distance.geodesic(driver_cors, customer_cors)
        if agent_distance < closest_distance:
            closest_distance = agent_distance
            closest_agent = agent
    
    # found the closest agent
    print(closest_agent)
    return closest_agent


@receiver(post_save, sender=OrderDelivery)
def order_assignment_to_agent(sender, instance, **kwargs):
    user_uuid = instance.delivery_agent.uuid
    logger.error(instance.delivery_agent)
    logger.error(user_uuid)
    order_notification_service = OrderAssignmentNotificationService(user_uuid, instance.order)
    order_notification_service.send_order_assignment_notification()
