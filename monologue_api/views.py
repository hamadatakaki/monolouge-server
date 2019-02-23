from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from monologue_api.models import Said, Action, Emotion
from monologue_api.serializers import SaidSerializer, ActionSerializer, EmotionSerializer

from accounts.models import Account

class SaidViewSet(viewsets.ModelViewSet):
    queryset = Said.objects.all().select_related()
    serializer_class = SaidSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all().select_related()
    serializer_class = ActionSerializer


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all().select_related()
    serializer_class = EmotionSerializer


@api_view(['GET'])
def timeline_view(request):
    user = request.user
    accounts = user.following_accounts.all()
    request_account = Account.objects.filter(username=user.username)

    saids = Said.objects.filter(account__in=(accounts | request_account)).order_by('datetime').reverse()
    serializer = SaidSerializer(saids, many=True)

    return Response(serializer.data)
