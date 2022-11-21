from django.db import models
from product.models import ProductsModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# one more table should be added for installment number 
# because there can be one installment order and multiple items

class InstallmentNumberModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateField()
    total_amount = models.IntegerField()
    balance = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return str(self.pk)


class InstallmentModel(models.Model):
    installmentNumber = models.ForeignKey(InstallmentNumberModel,on_delete=models.SET_DEFAULT,default=1)
    productId = models.ForeignKey(ProductsModel,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()
    approved = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    # status = models.TextChoices() this should have choices if paid or not paid

class ManufacturerInstallmentRecord(models.Model):
    productId = models.ForeignKey(ProductsModel,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()

class Cart(models.Model):
    product_id = models.ForeignKey(ProductsModel,on_delete=models.SET_DEFAULT,default=1)
    user = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()

