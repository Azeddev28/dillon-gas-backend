from django.contrib import admin
from apis.delivery_management.models import OrderDelivery

from apis.orders.models import Order, OrderItem
from apis.orders.utils.admin_restricted_field_choices import NON_EDITABLE_ORDER_STATUS


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    exclude = ['is_active', ]
    extra = 0


class OrderDeliveryAdminInline(admin.StackedInline):
    model = OrderDelivery
    exclude = ['is_active', ]
    # autocomplete_fields = ['delivery_agent',]
    extra = 1
    max_num = 1

    def get_field_queryset(self, db, db_field, request):
        queryset = super().get_field_queryset(db, db_field, request)
        if db_field.name == 'delivery_agent':
            queryset = queryset.filter(role='delivery_agent')

        return queryset


class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'order_number', 'order_status', 'created_at']
    readonly_fields = ['customer', 'order_number', 'base_price',
                       'total_price', 'customer_address', 'transaction']
    exclude = ['station', 'is_active']
    inlines = [OrderItemInline, OrderDeliveryAdminInline]

    def customer_address(self, instance):
        return instance.customer.user_addresses.filter(selected=True).first()

    class Meta:
        model = Order

    def get_readonly_fields(self, request, obj):
        fields = super().get_readonly_fields(request, obj)
        if obj and obj.order_status not in NON_EDITABLE_ORDER_STATUS:
            return fields

        fields.append('order_status')
        return set(fields)


admin.site.register(Order, OrderAdmin)
