from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


from monologue_api.models import Said, Action, Emotion
from monologue_api.serializers import (
    SaidSerializer, ActionSerializer, EmotionSerializer
)

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


@api_view(["GET"])
def timeline_view(request):
    user = request.user
    accounts = user.following_accounts.all()
    request_account = Account.objects.filter(username=user.username)

    saids = Said.objects.filter(account__in=(accounts | request_account)).order_by("datetime").reverse()
    serializer = SaidSerializer(saids, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def said_has_an_action(request, **kwargs):
    action_id = kwargs['id']
    try:
        action = Action.objects.get(id=action_id)
    except Action.DoesNotExist:
        return Response({
            "message": "not found the action"
        }, status=HTTP_400_BAD_REQUEST)
    saids = Said.objects.filter(action=action).order_by("datetime").reverse()
    serializer = SaidSerializer(saids, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def said_has_an_emotion(request, **kwargs):
    emotion_id = kwargs['id']
    try:
        emotion = Emotion.objects.get(id=emotion_id)
    except Emotion.DoesNotExist:
        return Response({
            "message": "not found the action"
        }, status=HTTP_400_BAD_REQUEST)
    saids = Said.objects.filter(emotion=emotion).order_by("datetime").reverse()
    serializer = SaidSerializer(saids, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["POST"])
def say_view(request):
    me = request.user
    data = request.data
    try:
        text = data["text"]
        action, _ = Action.objects.get_or_create(action=data["action"])
        emotion, _ = Emotion.objects.get_or_create(emotion=data["emotion"])
    except KeyError:
        return Response({
            "message": "サポートされないデータが入力されています"
        }, status=HTTP_400_BAD_REQUEST)

    said = Said.objects.create(
        text=text,
        account=me,
        datetime=timezone.now(),
        action=action,
        emotion=emotion
    )

    serializer = SaidSerializer(said)

    return Response(serializer.data, status=HTTP_200_OK)
