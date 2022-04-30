from django.contrib import admin

from apis.stations.models import Station, StationInventoryItem


admin.site.register(Station)
admin.site.register(StationInventoryItem)
