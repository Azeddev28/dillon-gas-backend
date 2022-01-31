from django.contrib import admin

from apis.deliveries.models import Delivery


class DeliveryAdmin(admin.ModelAdmin):

    list_display = ('delivery_agent', 'customer',  'order_placed',
                    'delivered_at', 'status')


admin.site.register(Delivery, DeliveryAdmin)
