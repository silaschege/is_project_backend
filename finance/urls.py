from django.urls import path
from .views import (
farmerMakePayment,
farmerPaymentHistory,
ManufacturerPaymentHistory,

)

urlpatterns = [
   
    path('farmerMakePayment/<id>',farmerMakePayment,name='farmerMakePayment'),
    path('farmerPaymentHistory',farmerPaymentHistory,name='farmerPaymentHistory'),
#######################################################################################################################
    path('ManufacturerPaymentHistory',ManufacturerPaymentHistory,name='ManufacturerPaymentHistory'),
]