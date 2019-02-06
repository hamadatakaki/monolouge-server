from rest_framework import serializers

from monologue_api.models import Said, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('action', 'emotion', )


class SaidSerialiser(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Said
        fields = ('text', 'datetime', 'status', 'account', )
