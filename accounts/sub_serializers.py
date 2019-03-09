from rest_framework import serializers

from accounts.models import Account


class AccountNameAndUuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('uuid', 'username')


class AccountFollowersSerializer(serializers.ModelSerializer):
    followers = AccountNameAndUuidSerializer(many=True)

    class Meta:
        model = Account
        fields = ('followers', )


class AccountProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('screen_name', 'bio')
