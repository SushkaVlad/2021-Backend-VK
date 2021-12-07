from rest_framework.routers import DefaultRouter
from cars.views import CarViewSet

router = DefaultRouter()
router.register('', CarViewSet, basename='car')
urlpatterns = router.urls
