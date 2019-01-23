from django.db import models
from django.utils import timezone


class Said(models.Model):
    text = models.TextField(max_length=140)
    datetime = models.DateTimeField(default=timezone.now)


class Status(models.Model):
    action = models.CharField(max_length=31, default="no action")
    emotion = models.CharField(max_length=31, default="no emotion")
