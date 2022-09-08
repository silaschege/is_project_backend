from .viewset import ManufactureRegisterViewSet
from rest_framework.routers import routers

manufacturer_router = routers.SimpleRouter()
manufacturer_router.register(r'manufacturerregister', ManufactureRegisterViewSet, basename='manufacturerregister')
urlpatterns = manufacturer_router.urls