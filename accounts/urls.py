from django.urls import path

from rest_framework import routers

from accounts.views import AccountViewSet, follow, get_uuid, get_info

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('follow/', follow),
    path('accounts/info/<str:name>/uuid/', get_uuid),
    path('accounts/info/<str:name>/', get_info)
]
