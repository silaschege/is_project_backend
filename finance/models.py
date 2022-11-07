from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from installments.models import InstallmentNumberModel


# Create your models here.
# there should be an improvement after adding plant categories for amount per category
class PaymentLogModel(models.Model):
    user_id =  models.ManyToManyField(User)
    installment_id = models.ManyToManyField(InstallmentNumberModel)
    amount  = models.FloatField(max_length=7)
    totalAmountPaid =  models.FloatField(max_length=7)
    balance  = models.FloatField(max_length=7)
    timePaid = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=255)
    
