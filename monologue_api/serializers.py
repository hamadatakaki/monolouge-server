from rest_framework import serializers

from monologue_api.models import Said, Status


class SaidSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Said
        fields = ('text', 'datetime', 'status', )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('action', 'emotion', )
