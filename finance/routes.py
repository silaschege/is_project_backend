from .viewset import PaymentLogViewSet
from rest_framework.routers import DefaultRouter

finance_router = DefaultRouter()
finance_router.register(r'payment', PaymentLogViewSet, basename='payment')
urlpatterns = finance_router.urls