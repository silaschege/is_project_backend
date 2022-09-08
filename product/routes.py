from .viewset import ProductCategoryViewSet,ProductModelViewSet
from rest_framework.routers import routers

products_router= routers.SimpleRouter()
products_router.register(r'ProductCategory',ProductCategoryViewSet, basename='ProductCategory')
products_router.register(r'ProductModel',ProductModelViewSet, basename='ProductModel')
urlpatterns = products_router.urls