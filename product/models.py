from django.utils.timezone import now
from django.db import models

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

class ProductModel(models.Model):
    productName = models.CharField(max_length=255)
    productCategory = models.ForeignKey(ProductCategoryModel,on_delete=models.CASCADE,)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=7)
    packagingQuantity = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)
    product_image = models.ImageField(upload_to='product_images/')

    # merchant foreign key needs to be added

    def __str__(self):
      return self.productName
