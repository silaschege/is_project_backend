from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from ..installments.models import InstallmentModel

# Create your models here.
class PaymentLogModel(models.Model):
    user_id =  models.ManyToManyField(User)
    insallment_id = models.ManyToManyField(InstallmentModel)
    amount  = models.FloatField(max_length=7)
    totalAmountPaid =  models.FloatField(max_length=7)
    balance  = models.FloatField(max_length=7)
    timePaid = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=255)
    
