from django.contrib import admin

from apis.inventory.models import Category, Item
from apis.stations.models import StationInventoryItem


class StationInventoryItemInline(admin.StackedInline):
    model = StationInventoryItem
    fields = ['quantity', 'price', 'tax']
    extra = 1
    max_num = 1
    can_delete = False



class ItemAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'quantity']
    inlines = [StationInventoryItemInline,]

    def quantity(self, obj):
        return obj.inventory.first().quantity

    class Meta:
        model = Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'item_count']

    def item_count(self, obj):
        return obj.category_items.count()

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
