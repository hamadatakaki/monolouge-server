from django.db import models
from django.utils import timezone


DEFAULT_ACTION_ID = 1
DEFAULT_EMOTION_ID = 1


def get_default_action():
    try:
        action, _ = Action.objects.get_or_create(action="no action")
    except Action.DoesNotExist:
        action = Action(action="no action")
        action.save()
    return action.pk


def get_default_emotion():
    try:
        emotion, _ = Emotion.objects.get_or_create(emotion="no emotion")
    except Emotion.DoesNotExist:
        emotion = Emotion(emotion="no emotion")
        emotion.save()
    return emotion.pk


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
    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="saids",
        blank=True,
        null=True,
    )
