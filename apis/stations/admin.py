from django.contrib import admin

from apis.stations.models import GasStation, Inventory


class GasStationAdmin(admin.ModelAdmin):

    list_display = ('station_id', 'city',  'owner',)


class InventoryAdmin(admin.ModelAdmin):

    list_display = ('item', 'price',  'quantity', 'station')


admin.site.register(GasStation, GasStationAdmin)
admin.site.register(Inventory, InventoryAdmin)
