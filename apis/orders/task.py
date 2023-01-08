import time
from apis.delivery_management.signals import find_closest_agent
from apis.delivery_management.models import OrderDelivery
import threading

class ThreadService(threading.Thread):
    def __init__(self, order):
        threading.Thread.__init__(self)
        self.order = order

    def run(self):
        # Sleep for 5 minutes to get all delivery agent locations
        time.sleep(5) # Number of seconds

        #find the closest agent
        closest_agent = find_closest_agent(None)
        OrderDelivery.objects.create(order=self.order, delivery_agent=closest_agent.user)
