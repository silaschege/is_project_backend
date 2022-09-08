from .viewset import InstallmentViewSet
from rest_framework.routers import routers

installments_router = routers.SimpleRouter()
installments_router.register(r'installment', InstallmentViewSet, basename='installment')
urlpatterns = installments_router.urls