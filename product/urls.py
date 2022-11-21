from django.urls import path
from .views import (FarmerInstallmentsListView,

FarmerAddPlantsList,
FarmerAddPlantsCategoryList,
ManufacturerStore,
ManufacturerAddProduct,
ManufacturerUpdateStore,
ManufacturerSelectUpdate,
ManufacturerAddProductNameView,
ManufacturerLoadProductsName,
ManufacturerProductNames,
AdminAddCategory,
AdminAddPackagingMetric,
AdminAddPackagingQuantity,
AdminAllProducts,
AdminAllCategory,
AdminAllPackagingMetric,
AdminAllPackagingQuantity,
AdminDeleteCategory,
AdminDeletePackagingMetric,
AdminDeletePackagingQuantity,
)

urlpatterns = [
    path('FarmerInstallmentListView',FarmerInstallmentsListView,name='FarmerInstallmentListView'),
    path('FarmerAddPlantsList/<category_id>',FarmerAddPlantsList,name='FarmerAddPlantsList'),
    path('FarmerAddPlantsCategoryList',FarmerAddPlantsCategoryList,name='FarmerAddPlantsCategoryList'),
    

    path('ManufacturerStore',ManufacturerStore,name='ManufacturerStore'),
    path('ManufacturerAddProduct',ManufacturerAddProduct,name='ManufacturerAddProduct'),
    path('ManufacturerAddProductName',ManufacturerAddProductNameView,name='ManufacturerAddProductName'),
    path('ManufacturerSelectUpdate/<product_id>',ManufacturerSelectUpdate,name='ManufacturerSelectUpdate'),
    path('ManufacturerUpdateStore/<product_id>',ManufacturerUpdateStore,name='ManufacturerUpdateStore'),
    path('ManufacturerLoadProductsName',ManufacturerLoadProductsName,name='ManufacturerLoadProductsName'),
    
    path('ManufacturerProductNames',ManufacturerProductNames,name='ManufacturerProductNames'),
   

    path('AdminAddCategoryU',AdminAddCategory,name='AdminAddCategoryU'),
    path('AdminAddPackagingMetric',AdminAddPackagingMetric,name='AdminAddPackagingMetric'),
    path('AdminAddPackagingQuantity',AdminAddPackagingQuantity,name='AdminAddPackagingQuantity'),
    path('AdminAllProducts',AdminAllProducts,name='AdminAllProducts'),
    path('AdminAllCategory',AdminAllCategory,name='AdminAllCategory'),
    path('AdminAllPackagingMetric',AdminAllPackagingMetric,name='AdminAllPackagingMetric'),
    path('AdminAllPackagingQuantity',AdminAllPackagingQuantity,name='AdminAllPackagingQuantity'),
    path('AdminDeleteCategory/<id>',AdminDeleteCategory,name='AdminDeleteCategory'),
    path('AdminDeletePackagingMetric/<id>',AdminDeletePackagingMetric,name='AdminDeletePackagingMetric'),
    path('AdminDeletePackagingQuantity/<id>',AdminDeletePackagingQuantity,name='AdminDeletePackagingQuantity'),


    
]
