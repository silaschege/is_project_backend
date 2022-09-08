from .viewset import LandRegisterViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'land', LandRegisterViewSet, basename='land')
urlpatterns = router.urls