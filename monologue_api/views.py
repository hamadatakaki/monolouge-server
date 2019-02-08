from rest_framework import viewsets

from monologue_api.models import Said, Action, Emotion
from monologue_api.serializers import SaidSerialiser, ActionSerializer, EmotionSerializer


class SaidViewSet(viewsets.ModelViewSet):
    queryset = Said.objects.all().select_related()
    serializer_class = SaidSerialiser


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all().select_related()
    serializer_class = ActionSerializer


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all().select_related()
    serializer_class = EmotionSerializer
