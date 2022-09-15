from .viewset import InstallmentViewSet
from rest_framework.routers import DefaultRouter

installments_router = DefaultRouter()
installments_router.register(r'installment', InstallmentViewSet, basename='installment')
urlpatterns = installments_router.urls