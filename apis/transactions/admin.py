from django.contrib import admin

from apis.transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):

    list_display = ('id', 'user',  'status',
                    'product', 'amount')


admin.site.register(Transaction, TransactionAdmin)
