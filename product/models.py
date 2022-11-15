from email.policy import default
from pyexpat import model
from django.utils.timezone import now
from django.db import models
from manufacturer.models import ManufactureRegisterModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class ProductCategoryModel(models.Model):
    categoryName = models.CharField(max_length=255)
    ProductCategory_image = models.ImageField(upload_to='productCategory_images/',default='media/product_images/Screenshot_2022-09-12_at_16.00.36.png')

    def __str__(self):
        return self.categoryName

# one more table should be added for the product 
# eg maize that will the be connected to the category and the product to the product type table
class ProductNameModel(models.Model):
    productCategory = models.ForeignKey(ProductCategoryModel,on_delete=models.SET_DEFAULT,default=1)
    productName = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.productName

class PackagingMetric(models.Model):
    packagingMetric = models.CharField(max_length=255)

    def __str__(self):
        return self.packagingMetric

#quantity should have choices like 5 and 10 
#packacking quantity should also have choices like litrs,kgs,mg

class PackagingQuantity(models.Model):
    packagingQuantity = models.IntegerField()

    def __str__(self):
        return str(self.packagingQuantity)


class ProductsModel (models.Model):
    productCategory = models.ForeignKey(ProductCategoryModel,on_delete=models.SET_DEFAULT,default=1)
    productName = models.ForeignKey(ProductNameModel,on_delete=models.SET_NULL, null=True)
    productManufacturer = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)
    productPrice = models.IntegerField()
    productPieces = models.IntegerField()
    productImage = models.ImageField(upload_to='product_images/',default='media/product_images/Screenshot_2022-09-12_at_16.00.36.png')
    packagingMetric = models.ForeignKey(PackagingMetric,on_delete=models.SET_DEFAULT,default=1)
    packagingQuantity = models.ForeignKey(PackagingQuantity,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.productName)
   

