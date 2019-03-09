from django.core.exceptions import ValidationError

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from accounts.models import Account
from accounts.serializers import AccountSerializer
from accounts.sub_serializers import AccountFollowersSerializer, AccountProfileSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


@api_view(['POST'])
def follow(request):
    me = request.user
    username = request.data["accountID"]

    if me.username != username:
        try:
            me.following_accounts.add(Account.objects.get(username=username))
        except ValidationError:
            return Response({
                "message": "the uuid does not exist."
            }, status=HTTP_400_BAD_REQUEST)

        mess = "you success to follow {}".format(username)
        status = HTTP_200_OK

    else:
        mess = "this is your account id : {}".format(username)
        status = HTTP_200_OK

    return Response({
        "message": mess
    }, status=status)


# excludeしたものをsetすれば良い
@api_view(['POST'])
def unfollow(request):
    me = request.user
    username = request.data["accountID"]

    if me.username != username:
        excluded = me.following_accounts.exclude(username=username)
        me.following_accounts.set(excluded)
        return Response({
            "message": f"you unfollow {username}"
        }, status=HTTP_200_OK)
    else:
        return Response({
            "message": f"this is your account id : {username}"
        }, status=HTTP_200_OK)


@api_view(["GET"])
def get_uuid(request, **kwargs):
    account_name = kwargs["name"]

    try:
        account = Account.objects.get(username=account_name)
    except Account.DoesNotExist:
        return Response({
            "message": "the account who has request name does not exist "
        })

    res = {
        "uuid": account.uuid
    }
    return Response(res, status=HTTP_200_OK)


@api_view(["GET"])
def get_info(request, **kwargs):
    account_name = kwargs["name"]

    try:
        account = Account.objects.get(username=account_name)
    except Account.DoesNotExist:
        return Response({
            "message": "the account who has request name does not exist "
        })

    serializer = AccountSerializer(account)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(["GET"])
def get_followers(request, **kwargs):
    account_name = kwargs["name"]

    try:
        account = Account.objects.get(username=account_name)
    except Account.DoesNotExist:
        return Response({
            "message": "the account who has request name does not exist "
        })

    serializer = AccountFollowersSerializer(account)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['PUT'])
def edit_profile(request, **kwargs):
    account_name = kwargs["name"]

    try:
        account = Account.objects.get(username=account_name)
    except Account.DoesNotExist:
        return Response({
            "message": "the account who has request name does not exist"
        })

    serializer = AccountProfileSerializer(account, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
