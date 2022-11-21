from urllib3 import request
from django.db.models.signals import pre_save,post_save
from .models import InstallmentNumberModel,InstallmentModel
from shipping.models import ShippingRegister
from django.dispatch import receiver

@receiver(post_save,sender=InstallmentNumberModel)

def postSaveShipping(sender,instance,*args,**kwargs):  
    balance = instance.balance
    print(balance)
    if int(balance) <= 0:
        ShippingRegister.objects.create(installment=instance)
    
    print('check if shipping is zero')