from django.urls import path
from .views import CreateShippingView,UpdateShipping

urlpatterns = [
    path('createShipping',CreateShippingView.as_view()),
    path('updateShipping',UpdateShipping.as_view()),
]