from django.db import models
from django.utils import timezone


# 可能なら別の実装を考える（てか知りたい
# get_or_createでtry-except書いておいて、失敗したらID使うのが良さそう？
DEFAULT_ACTION_ID = 1
DEFAULT_EMOTION_ID = 1


def get_default_action():
    try:
        action, _ = Action.objects.get_or_create(action="no action")
        return action.pk
    except Exception:
        return DEFAULT_ACTION_ID


def get_default_emotion():
    try:
        emotion, _ = Emotion.objects.get_or_create(emotion="no emotion")
        return emotion.pk
    except Exception:
        return DEFAULT_EMOTION_ID


class Action(models.Model):
    action = models.CharField(max_length=31, default="no action")


class Emotion(models.Model):
    emotion = models.CharField(max_length=31, default="no emotion")


class Said(models.Model):
    text = models.TextField(max_length=140)
    datetime = models.DateTimeField(default=timezone.now)
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
        related_name="saids",
        default=get_default_action,
    )
    emotion = models.ForeignKey(
        Emotion,
        on_delete=models.CASCADE,
        related_name="saids",
        default=get_default_emotion,
    )


