from pyexpat import model
from django.utils.timezone import now
from django.db import models
from manufacturer.models import ManufactureRegisterModel

# Create your models here.
class ProductCategoryModel(models.Model):
    # class categoryTypeChoices(models.Choices):
    #     Herbivorous= 'herbivrous'
    #     Seed = 'seed'
    #     Pesticide = 'pesticide'
    # categoryName = models.CharField(max_length=255,choices=categoryTypeChoices,default=Seed)
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryName

# one more table should be added for the product 
# eg maize that will the be connected to the category and the product to the product type table
class ProductNameModel(models.Model):
    productName = models.CharField(max_length=255)

    def __str__(self):
        return self.productName

# quantity should have choices like 5 and 10 
#  packacking quantity should also have choices like litrs,kgs,mg
class ProductModel(models.Model):
    productName = models.ManyToManyField(ProductNameModel)
    productCategory = models.ForeignKey(ProductCategoryModel,on_delete=models.CASCADE,)
    manufacturer = models.ManyToManyField(ManufactureRegisterModel)
    price = models.FloatField(max_length=7)
    quantity = models.IntegerField()
    packagingQuantity = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)
    product_image = models.ImageField(upload_to='product_images/')
    

    # merchant foreign key needs to be added

    def __str__(self):
      return str(self.productName)

