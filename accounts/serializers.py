from rest_framework import serializers

from accounts.models import Account
from monologue_api.serializers import SaidSerializer, ActionSerializer, EmotionSerializer


class AccountProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'screen_name',
            'username',
            'bio'
        )


class AccountSaidSerializer(serializers.ModelSerializer):
    saids = SaidSerializer(many=True)

    class Meta:
        model = Account
        fields = ('saids', )


# class AccountImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ('origin', )
