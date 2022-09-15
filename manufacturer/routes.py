from .viewset import ManufactureRegisterViewSet
from rest_framework.routers import DefaultRouter

manufacturer_router = DefaultRouter()
manufacturer_router.register(r'manufacturerregister', ManufactureRegisterViewSet, basename='manufacturerregister')
urlpatterns = manufacturer_router.urls