from django.urls import path

from rest_framework import routers

from accounts.views import AccountViewSet

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = []
