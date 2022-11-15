from django.urls import path
from .views import (FarmerAddInstallmentHolder,
farmerCart,
farmerCartRemove,
farmerCreateInstallmentNumber,
FarmerCreateInstallment,
FarmerInstallmentDetailView,
ManufacturerAllInstallment,
ManufacturerAllInstallmentReport 
)
urlpatterns = [
    path('FarmerAddInstallmentHolder/<product_id>',FarmerAddInstallmentHolder,name='FarmerAddInstallmentHolder'),
    path('farmerCartRemove/<product_id>',farmerCartRemove,name='farmerCartRemove'),
    path('farmerCart',farmerCart,name='farmerCart'),
    path('farmerCreateInstallmentNumber/<alltotals>',farmerCreateInstallmentNumber,name='farmerCreateInstallmentNumber'),
    path('FarmerCreateInstallment',FarmerCreateInstallment,name='FarmerCreateInstallment'),
    path('FarmerInstallmentDetailView/<id>',FarmerInstallmentDetailView,name='FarmerInstallmentDetailView'),
#######################################################################################################################
    path('ManufacturerAllInstallment',ManufacturerAllInstallment,name='ManufacturerAllInstallment'),
    path('ManufacturerAllInstallmentReport',ManufacturerAllInstallmentReport,name='ManufacturerAllInstallmentReport'),
]