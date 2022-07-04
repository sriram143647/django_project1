from team.views import TeamViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("team", TeamViewSet)
urlpatterns = router.urls

