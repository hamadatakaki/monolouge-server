from rest_framework import routers

from monologue_api import views


router = routers.DefaultRouter()
router.register('saids', views.SaidViewSet)
router.register('statuses', views.StatusViewSet)
