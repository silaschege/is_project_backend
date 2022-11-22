from django import forms
from django.forms import ModelForm
from .models import ProductsModel,ProductCategoryModel,PackagingMetric,PackagingQuantity,ProductNameModel

##############################################################################################################################
class  ManufacturerAddProductForm(ModelForm):
    class Meta:
        model = ProductsModel
        fields = ('productCategory','productName','productPrice','productPieces','productImage','packagingMetric','packagingQuantity')




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['productName'].queryset = ProductNameModel.objects.none()
    
        if 'productCategory' in self.data:
            try:
                productCategory_id = int(self.data.get('productCategory'))
                self.fields['productName'].queryset = ProductNameModel.objects.filter(productCategory_id=productCategory_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty productName queryset
    # elif self.instance.pk:
    #         self.fields['productName'].queryset = self.instance.productCategory.productName_set.order_by('name')



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
    
class ManufacturerAddProductName(ModelForm):
    class Meta:
        model = ProductNameModel
        fields = ('productName','productCategory')
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
