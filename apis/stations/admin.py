from django.contrib import admin

from apis.stations.models import Station, StationInventoryItem

class StationInventoryItemAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'item', 'quantity']
    class Meta:
        model = StationInventoryItem

# admin.site.register(Station)
admin.site.register(StationInventoryItem, StationInventoryItemAdmin)
