from django.urls import path

from rest_framework import routers

from accounts.views import AccountViewSet, follow, unfollow,  get_info, get_followers, edit_profile

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('follow/', follow),
    path('unfollow/', unfollow),
    path('accounts/<str:name>/info/', get_info),
    # path('accounts/<str:name>/uuid/', get_uuid),  # TODO リファクタリング後 必要無かったら消す
    path('accounts/<str:name>/followers/', get_followers),
    path('accounts/<str:name>/edit/', edit_profile)
]
