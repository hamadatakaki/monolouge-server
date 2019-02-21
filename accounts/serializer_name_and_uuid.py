from rest_framework import serializers

from accounts.models import Account


class AccountNameAndUuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('uuid', 'username')
