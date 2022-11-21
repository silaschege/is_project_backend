from django.urls import path
from .views import (FarmerAddInstallmentHolder,
farmerCart,
FarmerCartRemove,
farmerCreateInstallmentNumber,
FarmerCreateInstallment,
FarmerInstallmentDetailView,
ManufacturerAllInstallment,
ManufacturerAllInstallmentReport,
AdminAllInstallmentsNumber,

)
urlpatterns = [
    path('FarmerAddInstallmentHolder/<product_id>',FarmerAddInstallmentHolder,name='FarmerAddInstallmentHolder'),
    path('FarmerCartRemove/<id>',FarmerCartRemove,name='FarmerCartRemove'),
    path('farmerCart',farmerCart,name='farmerCart'),
    path('farmerCreateInstallmentNumber/<alltotals>',farmerCreateInstallmentNumber,name='farmerCreateInstallmentNumber'),
    path('FarmerCreateInstallment',FarmerCreateInstallment,name='FarmerCreateInstallment'),
    path('FarmerInstallmentDetailView/<id>',FarmerInstallmentDetailView,name='FarmerInstallmentDetailView'),
#######################################################################################################################
    path('ManufacturerAllInstallment',ManufacturerAllInstallment,name='ManufacturerAllInstallment'),
    path('ManufacturerAllInstallmentReport',ManufacturerAllInstallmentReport,name='ManufacturerAllInstallmentReport'),
#######################################################################################################################
    path('AdminAllInstallmentsNumber',AdminAllInstallmentsNumber,name='AdminAllInstallmentsNumber'),
]