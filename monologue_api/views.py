from rest_framework import viewsets

from monologue_api.models import Said, Status
from monologue_api.serializers import SaidSerialiser, StatusSerializer


class SaidViewSet(viewsets.ModelViewSet):
    queryset = Said.objects.all().select_related()
    serializer_class = SaidSerialiser


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().select_related()
    serializer_class = StatusSerializer
