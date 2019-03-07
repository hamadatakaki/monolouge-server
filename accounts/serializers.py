from rest_framework import serializers

from accounts.models import Account
from monologue_api.serializers import SaidSerializer


class AccountSerializer(serializers.ModelSerializer):
    saids = SaidSerializer(many=True)

    class Meta:
        model = Account
        fields = (
            'screen_name',
            'username',
            'bio',
            'saids',
        )
