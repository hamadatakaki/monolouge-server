from rest_framework import serializers

from accounts.models import Account
from monologue_api.serializers import SaidSerialiser, StatusSerializer


class AccountSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Account
        fields = (
            'screen_name',
            'username',
            'email',
            'bio',
            'said',
            'status',
            'following_accounts',
        )
