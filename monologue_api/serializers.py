from rest_framework import serializers

from monologue_api.models import Said, Action, Emotion
from accounts.sub_serializers import AccountNameAndUuidSerializer


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action')


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('id', 'emotion',)


class SaidSerializer(serializers.ModelSerializer):
    action = ActionSerializer()
    emotion = EmotionSerializer()
    account = AccountNameAndUuidSerializer()

    class Meta:
        model = Said
        fields = ('id', 'text', 'datetime', 'action', 'emotion', 'account', )
