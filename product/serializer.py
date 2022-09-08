from dataclasses import fields
from pyexpat import model
from turtle import mode
from rest_framework import serializers
from .models import ProductCategoryModel,ProductModel

class ProductCategorySerializer(serializers.Serializer):
    class Meta:
        model = ProductCategoryModel
        fields = "__all__"


class ProductModelSerializer(serializers.Serializer):
    class Meta:
        model = ProductModel
        fields = "__all__"