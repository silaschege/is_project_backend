from django.urls import path
from .views import (
    FarmerReceiveShipping_Receive,
    FarmerShippingHistory,
    FarmerReceiveShipping,
    FarmercurrentShipping,
    ManufacturerShippingApproval,
    ManufacturerShippingApproval_Approval,
    ManufacturerReceivedShipping,
    )

urlpatterns = [
    path('FarmercurrentShipping',FarmercurrentShipping,name='FarmercurrentShipping'),
    path('FarmerReceiveShipping',FarmerReceiveShipping,name='FarmerReceiveShipping'),
    path('FarmerReceiveShipping_Receive/<id>',FarmerReceiveShipping_Receive,name='FarmerReceiveShipping_Receive'),
    path('FarmerShippingHistory',FarmerShippingHistory,name='FarmerShippingHistory'),
################################################################################################################################
    path('ManufacturerShippingApproval',ManufacturerShippingApproval,name='ManufacturerShippingApproval'),
    path('ManufacturerShippingApproval_Approval/<id>',ManufacturerShippingApproval_Approval,name='ManufacturerShippingApproval_Approval'),
    path('ManufacturerReceivedShipping',  ManufacturerReceivedShipping,name='ManufacturerReceivedShipping'),

  
]