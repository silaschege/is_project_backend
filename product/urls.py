from django.urls import path
from .views import (FarmerInstallmentsListView,

FarmerAddPlantsList,
FarmerAddPlantsCategoryList,
ManufacturerStore,
ManufacturerAddProduct,
ManufacturerUpdateStore,
ManufacturerSelectUpdate,
AdminAddCategory,
AdminAddPackagingMetric,
AdminAddPackagingQuantity
)

urlpatterns = [
    path('FarmerInstallmentListView',FarmerInstallmentsListView,name='FarmerInstallmentListView'),
    path('FarmerAddPlantsList/<category_id>',FarmerAddPlantsList,name='FarmerAddPlantsList'),
    path('FarmerAddPlantsCategoryList',FarmerAddPlantsCategoryList,name='FarmerAddPlantsCategoryList'),
    

    path('ManufacturerStore',ManufacturerStore,name='ManufacturerStore'),
    path('ManufacturerAddProduct',ManufacturerAddProduct,name='ManufacturerAddProduct'),
    path('ManufacturerSelectUpdate/<product_id>',ManufacturerSelectUpdate,name='ManufacturerSelectUpdate'),
    path('ManufacturerUpdateStore/<product_id>',ManufacturerUpdateStore,name='ManufacturerUpdateStore'),
   

    path('AdminAddCategoryU',AdminAddCategory,name='AdminAddCategoryU'),
    path('AdminAddPackagingMetric',AdminAddPackagingMetric,name='AdminAddPackagingMetric'),
    path('AdminAddPackagingQuantity',AdminAddPackagingQuantity,name='AdminAddPackagingQuantity'),


    
]
