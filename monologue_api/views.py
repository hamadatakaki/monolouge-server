from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

# TODO 必要なAPIを絞る・Timeline用のAPIの実装
# example https://qiita.com/suzuesa/items/30bcbe6a7b2b2de1df25


@api_view(["GET"])
def timeline_view(request):
    user = request.user
    following_accounts = user.following_accounts.all()

    saids = Said.objects.filter(account__in=following_accounts).order_by('datetime')
    serializer = SaidSerialiser(saids, many=True)

    return Response(serializer.data)
