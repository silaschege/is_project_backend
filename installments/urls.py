from django.urls import path
from .views import AddInstallments,RemoveInstallment,UpdateInstallmentQuantity
urlpatterns = [
    path('addInstallment',AddInstallments.as_view()),
    path('removeInstallment',RemoveInstallment.as_view()),
    path('updateInstallment',UpdateInstallmentQuantity.as_view()),
]