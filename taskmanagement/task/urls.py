from rest_framework import routers

from task.views import TaskViewSet

router = routers.DefaultRouter()
router.register("task", TaskViewSet)
urlpatterns = router.urls



