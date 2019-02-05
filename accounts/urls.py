from django.urls import path

from rest_framework import routers

from accounts.views import AccountViewSet, login

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('login/', login),
]
