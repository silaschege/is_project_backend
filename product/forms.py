from tkinter import Widget
from pyexpat import model
from dataclasses import fields
from random import choices
from django import forms
from django.forms import ModelForm
from .models import ProductsModel,ProductCategoryModel,PackagingMetric,PackagingQuantity

##############################################################################################################################
class  ManufacturerAddProductForm(ModelForm):
    class Meta:
        model = ProductsModel
        fields = ('productCategory','productName','productPrice','productPieces','productImage','packagingMetric','packagingQuantity')
        # fields = ('__all__')

        labels={
            'productCategory':'Product Category',
            'productName':'Product Name',
            'productPrice':'Product Price',
            'productPieces':'ProductPieces',
            'productImage':'Product Image',
            'packagingMetric':'Packaging Metric',
            'packagingQuantity':'Packaging Quantity',
        }

        widgets ={
            'productCategory':forms.Select(attrs={'class':'form-select', 'placeholder':'Product Category'}) ,
            'productName':forms.Select(attrs={'class':'form-select', 'placeholder':'Product Name'}),
            'productPrice': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'productPieces':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Pieces'}),
            'packagingMetric':forms.Select(attrs={'class':'form-select', 'placeholder':'Packaging Metric'}),
            'packagingQuantity':forms.Select(attrs={'class':'form-select', 'placeholder':'Packaging Quantity'}),

        }
#########################################################################################################################
class AdminAddCategoryForm(ModelForm):
    class Meta:
        model = ProductCategoryModel
        fields =('categoryName','ProductCategory_image') 
        labels={
        'categoryName':'Category Name',
        'ProductCategory_image':'Category Image'
        }
        widget={
            'categoryName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category Name'}),
        }

class AdminAddProductPackagingMetric(ModelForm):
    class Meta:
        model = PackagingMetric
        fields = ('packagingMetric',)
        labels = {
                'packagingMetric':'Packaging Metric'
        }
        widget = {
            'packagingMetric':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Packaging Metric'}),
        }


class AdminAddProductPackagingQuantity(ModelForm):
    class Meta:
        model = PackagingQuantity
        fields = ('packagingQuantity',)
        labels = {
           'packagingQuantity':'packagingQuantity' 
        }
        widget = {
            'packagingQuantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Packaging Quantity'}),
        }
