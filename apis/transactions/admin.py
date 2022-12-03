from django.contrib import admin

from apis.transactions.models import Transaction
from apis.transactions.utils.constants import NON_EDITABLE_TRANSACTION_STATUS


class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['reference', 'user', 'amount']
    list_display = ['reference', 'user', 'amount', 'status']

    class Meta:
        model = Transaction

    def get_readonly_fields(self, request, obj):
        fields = super().get_readonly_fields(request, obj)
        if obj.status not in NON_EDITABLE_TRANSACTION_STATUS:
            return fields

        fields.append('status')
        return set(fields)

admin.site.register(Transaction, TransactionAdmin)
