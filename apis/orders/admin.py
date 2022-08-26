from django.contrib import admin

from apis.orders.models import Order, OrderItem
from apis.orders.utils.admin_restricted_field_choices import NON_EDITABLE_ORDER_STATUS

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    exclude = ['is_active',]
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'order_number', 'order_status', 'created_at']
    readonly_fields = ['customer', 'order_number', 'base_price', 'total_price', 'customer_address', 'transaction']
    exclude = ['station',]
    inlines = [OrderItemInline]

    def customer_address(self, instance):
        return instance.customer.user_addresses.filter(selected=True).first()

    class Meta:
        model = Order

    def get_readonly_fields(self, request, obj):
        fields = super().get_readonly_fields(request, obj)
        if obj.order_status not in NON_EDITABLE_ORDER_STATUS:
            return fields

        fields.append('order_status')
        return set(fields)


admin.site.register(Order, OrderAdmin)
