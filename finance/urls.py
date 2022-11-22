from django.urls import path
from .views import (
farmerMakePayment,
farmerPaymentHistory,
farmerAllPayment,
ManufacturerPaymentHistory,
ManufacturerShippingpayment,
AdminAllFarmerPayment,
AdminAllManufacturerPaid,

)

urlpatterns = [
   
    path('farmerMakePayment/<id>',farmerMakePayment,name='farmerMakePayment'),
    path('farmerPaymentHistory',farmerPaymentHistory,name='farmerPaymentHistory'),
     path('farmerAllPayment',farmerAllPayment,name='farmerAllPayment'),
#######################################################################################################################
    path('ManufacturerPaymentHistory',ManufacturerPaymentHistory,name='ManufacturerPaymentHistory'),
    path('ManufacturerShippingpayment',ManufacturerShippingpayment,name='ManufacturerShippingpayment'),
#######################################################################################################################
    path('AdminAllFarmerPayment',AdminAllFarmerPayment,name='AdminAllFarmerPayment'),
    path('AdminAllManufacturerPaid',AdminAllManufacturerPaid,name='AdminAllManufacturerPaid'),
]