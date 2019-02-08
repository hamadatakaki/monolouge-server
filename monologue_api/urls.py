from rest_framework import routers

from monologue_api.views import ActionViewSet, EmotionViewSet, SaidViewSet


router = routers.DefaultRouter()
router.register('saids', SaidViewSet)
router.register('actions', ActionViewSet)
router.register('emotions', EmotionViewSet)
