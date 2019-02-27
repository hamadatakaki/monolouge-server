from rest_framework import serializers

from accounts.models import Account
from monologue_api.serializers import SaidSerializer, ActionSerializer, EmotionSerializer


class AccountSerializer(serializers.ModelSerializer):
    action = ActionSerializer()
    emotion = EmotionSerializer()
    saids = SaidSerializer(many=True)

    class Meta:
        model = Account
        fields = (
            'screen_name',
            'username',
            'bio',
            'saids',
            'action',
            'emotion'
        )
