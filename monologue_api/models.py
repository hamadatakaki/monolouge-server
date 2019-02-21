from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    action = models.CharField(
        _('action'),
        max_length=31,
        default="no action"
    )


class Emotion(models.Model):
    emotion = models.CharField(
        _('emotion'),
        max_length=31,
        default="no emotion"
    )


class Said(models.Model):
    text = models.TextField(_('本文'), max_length=140)
    datetime = models.DateTimeField(_('投稿日時'), default=timezone.now)
    action = models.ForeignKey(
        Action,
        verbose_name=_('action'),
        on_delete=models.SET_DEFAULT,
        related_name="saids",
        default=get_default_action,
    )
    emotion = models.ForeignKey(
        Emotion,
        verbose_name=_('emotion'),
        on_delete=models.SET_DEFAULT,
        related_name="saids",
        default=get_default_emotion,
    )
    account = models.ForeignKey(
        "accounts.Account",
        verbose_name=_('account'),
        on_delete=models.CASCADE,
        related_name="saids",
        blank=True,
        null=True,
    )
