from django.urls import path
from .views import (MakePayment,
farmerMakePayment,
farmerPaymentHistory,
ManufacturerPaymentHistory,

)

urlpatterns = [
    path('makePayment',MakePayment.as_view()),
    path('farmerMakePayment/<id>',farmerMakePayment,name='farmerMakePayment'),
    path('farmerPaymentHistory',farmerPaymentHistory,name='farmerPaymentHistory'),
#######################################################################################################################
    path('ManufacturerPaymentHistory',ManufacturerPaymentHistory,name='ManufacturerPaymentHistory'),
]