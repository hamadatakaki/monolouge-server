from django.urls import path

from rest_framework import routers

from accounts.views import AccountViewSet, follow, get_uuid, account_saids

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('follow/', follow),
    path('accounts/<str:name>/uuid/', get_uuid),
    path('accounts/<str:uuid>/saids', account_saids),
    # path('accounts/<str:uuid>/icon', edit_profile_image)
]
