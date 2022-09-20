from django.db import models
from product.models import ProductModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# one more table should be added for installment number 
# because there can be one installment order and multiple items

class InstallmentNumberModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_date = models.DateField()
    total_amount = models.IntegerField()
    user_id = models.ManyToManyField(User)

class InstallmentModel(models.Model):
    installmentNumber = models.ManyToManyField(InstallmentNumberModel)
    product_id = models.ManyToManyField(ProductModel)
    quantity = models.IntegerField()
    # status = models.TextChoices() this should have choices if paid or not paid


