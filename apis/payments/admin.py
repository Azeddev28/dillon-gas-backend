from django.contrib import admin

from apis.payments.models import Wallet


class WalletAdmin(admin.ModelAdmin):

    list_display = ('wallet_id', 'user',  'amount',)


admin.site.register(Wallet, WalletAdmin)
