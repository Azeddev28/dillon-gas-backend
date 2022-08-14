from django.contrib import admin

from apis.orders.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ['name', 'uuid']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'order_key', 'created_at']
    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
