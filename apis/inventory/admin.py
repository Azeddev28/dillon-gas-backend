from django.contrib import admin

from apis.inventory.models import Category, Item, ItemQualification


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemQualification)
