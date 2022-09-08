from xml.parsers.expat import model
from rest_framework import viewsets
from .models import ProductCategoryModel,ProductModel
from .serializer import ProductCategorySerializer,ProductModelSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategoryModel.objects.all()
    serializer = ProductCategorySerializer

class ProductModelViewSet(viewsets.ViewSet):
    queryset = ProductModel.objects.all()
    serializer = ProductModelSerializer