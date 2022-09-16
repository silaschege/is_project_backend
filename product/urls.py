from django.urls import path
from .views import RetrieveProductFarmer,RetrieveProductsManufacturer,AddNewProductManufacturer,DeleteProduct

urlpatterns = [
    path('retrieveProductManufacturer',RetrieveProductsManufacturer.as_view()),
    path('retrieveProductFarmer',RetrieveProductFarmer.as_view()),
    path('addProduct',AddNewProductManufacturer.as_view()),
    path('deleteProduct',DeleteProduct.as_view()),
]
