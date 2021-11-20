from rest_framework.routers import DefaultRouter
from automakers.views import AutoMakerViewSet
router = DefaultRouter()
router.register('', AutoMakerViewSet, basename='automaker')
urlpatterns = router.urls

