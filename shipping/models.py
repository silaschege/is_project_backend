from django.db import models
from installments.models import InstallmentNumberModel
from django.utils.timezone import now
from django.contrib.auth import get_user_model

# Create your models here.
# there should be choices for shipping status
# there should be an updated at row
class ShippingRegister(models.Model):

    installment = models.ForeignKey(InstallmentNumberModel,on_delete=models.SET_DEFAULT,default=1)
    created_at = models.DateTimeField(default=now)
