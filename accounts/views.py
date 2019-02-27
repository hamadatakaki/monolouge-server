from django.core.exceptions import ValidationError

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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
        status = HTTP_200_OK

    else:
        mess = "this is your id: {}".format(uuid)
        status = HTTP_200_OK

    return Response({
        "message": mess
    }, status=status)


@api_view(["GET"])
def get_uuid(request, **kwargs):
    account_name = kwargs["name"]

    try:
        account = Account.objects.get(username=account_name)
    except Account.DoesNotExist:
        return Response({
            "message": "the account who has request name does not exist."
        })

    res = {
        "uuid": account.uuid
    }
    return Response(res, status=HTTP_200_OK)
