from rest_framework import routers
from testeDjango.views import ToDoViewSet

router = routers.DefaultRouter()
router.register(r'api', ToDoViewSet)

urlpatterns = router.urls