from django.urls import path
from .views import MakePayment

urlpatterns = [
    path('makePayment',MakePayment.as_view())
]