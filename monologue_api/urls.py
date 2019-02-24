from django.urls import path

from rest_framework import routers

from monologue_api.views import (
    ActionViewSet, EmotionViewSet, SaidViewSet,
    timeline_view, say_view, said_has_an_action, said_has_an_emotion
)


router = routers.DefaultRouter()
router.register('saids', SaidViewSet)
router.register('actions', ActionViewSet)
router.register('emotions', EmotionViewSet)

urlpatterns = [
    path("timeline/", timeline_view),
    path("say/", say_view),
    path("actions/<int:id>/saids/", said_has_an_action),
    path("emotions/<int:id>/saids/", said_has_an_emotion)
]
