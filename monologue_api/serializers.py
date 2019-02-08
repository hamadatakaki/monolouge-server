from rest_framework import serializers

from monologue_api.models import Said, Action, Emotion


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('action',)


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion',)


class SaidSerialiser(serializers.ModelSerializer):
    action = ActionSerializer()
    emotion = EmotionSerializer()

    class Meta:
        model = Said
        fields = ('text', 'datetime', 'action', 'emotion', 'account', )
