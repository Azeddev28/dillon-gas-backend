from django.contrib import admin

from apis.stations.models import Station, StationInventory


admin.site.register(Station)
admin.site.register(StationInventory)
