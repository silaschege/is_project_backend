from .viewset import LandRegisterViewSet
from rest_framework.routers import routers

land_router = routers.SimpleRouter()
land_router.register(r'landregister', LandRegisterViewSet, basename='landregister')
urlpatterns = land_router.urls