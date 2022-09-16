from django.urls import path
from .views import ManufactureRegisterCreateView,ManufactureRegisterUpdateView

urlpatterns = [
    path('createManufacturer',ManufactureRegisterCreateView.as_view()),
    path('updateManufacturer',ManufactureRegisterUpdateView.as_view()),
]