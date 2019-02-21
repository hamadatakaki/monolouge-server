from rest_framework import serializers

from monologue_api.models import Said, Action, Emotion
from accounts.serializer_name_and_uuid import AccountNameAndUuidSerializer


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('action',)


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion',)


class SaidSerializer(serializers.ModelSerializer):
    action = ActionSerializer()
    emotion = EmotionSerializer()
    account = AccountNameAndUuidSerializer()

    class Meta:
        model = Said
        fields = ('text', 'datetime', 'action', 'emotion', 'account', )
