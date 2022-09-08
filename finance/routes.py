from .viewset import PaymentLogViewSet
from rest_framework.routers import routers

finance_router = routers.SimpleRouter()
finance_router.register(r'payment', PaymentLogViewSet, basename='payment')
urlpatterns = finance_router.urls