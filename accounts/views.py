from django.core.exceptions import ValidationError

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from accounts.models import Account
from accounts.serializers import AccountProfileSerializer, AccountImageSerializer, AccountSaidSerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountProfileSerializer


@api_view(['GET'])
def account_saids(request, **kwargs):
    try:
        account = Account.objects.get(uuid=kwargs["uuid"])
    except Account.DoesNotExist:
        return Response({
            "message": "requested uuid does not exist"
        }, status=HTTP_400_BAD_REQUEST)

    serializer = AccountSaidSerializer(account)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def follow(request):
    me = request.user
    uuid = request.data["uuid"]

    if str(me.uuid) != uuid:
        try:
            me.following_accounts.add(Account.objects.get(uuid=uuid))
        except ValidationError:
            return Response({
                "message": "the uuid does not exist."
            }, status=HTTP_400_BAD_REQUEST)
        mess = "you success to follow {}".format(uuid)
    else:
        mess = "this is your id: {}".format(uuid)

    return Response({
        "message": mess
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


# @api_view(["GET", "PUT"])
# def edit_profile_image(request, **kwargs):
#     me = request.user
#     if request.method == "GET":
#         serializer = AccountImageSerializer(me)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = AccountImageSerializer(me, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
