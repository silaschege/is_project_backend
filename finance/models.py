from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from installments.models import InstallmentNumberModel


# Create your models here.
# there should be an improvement after adding plant categories for amount per category
class PaymentLogModel(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)
    installment_id = models.ForeignKey(InstallmentNumberModel,on_delete=models.SET_DEFAULT,default=1)
    amount  = models.FloatField(max_length=7)
    timePaid = models.DateTimeField(auto_now_add=True)
    
    
