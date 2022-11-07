from django.urls import path
from .views import FarmerAddInstallmentHolder,farmerCart,farmerCartRemove,createInstallmentHolder
urlpatterns = [
    path('FarmerAddInstallmentHolder/<product_id>',FarmerAddInstallmentHolder,name='FarmerAddInstallmentHolder'),
    path('farmerCartRemove/<product_id>',farmerCartRemove,name='farmerCartRemove'),
    path('farmerCart',farmerCart,name='farmerCart'),
    path('createInstallmentHolder/<alltotals>',createInstallmentHolder,name='createInstallmentHolder'),
    
]