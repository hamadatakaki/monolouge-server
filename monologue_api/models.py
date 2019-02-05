from django.db import models
from django.utils import timezone

# 可能なら別の実装を考える（てか知りたい
# get_or_createでtry-except書いておいて、失敗したらID使うのが良さそう？
DEFAULT_STATUS_ID = 1


class Status(models.Model):
    action = models.CharField(max_length=31, default="no action")
    emotion = models.CharField(max_length=31, default="no emotion")


class Said(models.Model):
    text = models.TextField(max_length=140)
    datetime = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=DEFAULT_STATUS_ID,
    )

# TODO Saidを取得した際に、Statusを展開して返すようにSerializerを設定する
