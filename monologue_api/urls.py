from django.urls import path

from rest_framework import routers

from monologue_api.views import ActionViewSet, EmotionViewSet, SaidViewSet, timeline_view


router = routers.DefaultRouter()
router.register('saids', SaidViewSet)
router.register('actions', ActionViewSet)
router.register('emotions', EmotionViewSet)

urlpatterns = [
    path("timeline/", timeline_view)
]
