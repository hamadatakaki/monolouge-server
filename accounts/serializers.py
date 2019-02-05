from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'screen_name',
            'username',
            'email',
            'bio',
            'said',
            'status',
        )
