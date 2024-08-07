from django.contrib.auth import get_user_model

from rest_framework import serializers

from apis.transactions.models import Transaction

User = get_user_model()


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), 
        queryset=User.objects.all(),
        write_only=True
    )

    class Meta:
        model = Transaction
        exclude = ['id']
