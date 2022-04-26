from django.contrib import admin

from apis.inventory.models import Category, Item


admin.site.register(Category)
admin.site.register(Item)
