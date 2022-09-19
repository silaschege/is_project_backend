from django.db import models
from installments.models import InstallmentModel
from django.utils.timezone import now

# Create your models here.
# there should be choices for shipping status
# there should be an updated at row
class ShippingRegister(models.Model):
    installment = models.ManyToManyField(InstallmentModel)
    Shipping_status  = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)
