from django.db import models
from installments.models import InstallmentNumberModel
from django.utils.timezone import now

# Create your models here.
# there should be choices for shipping status
# there should be an updated at row
class ShippingRegister(models.Model):
    SHIPPING = 'SH'
    INTRANSIT = 'IT'
    RECEIVED = 'REC'
    status_choices = [
        (SHIPPING,'SHIPPING'),
        (INTRANSIT,'INTRANSIT'),
        (RECEIVED,'RECEIVED'),
    ]
    installment = models.ForeignKey(InstallmentNumberModel,on_delete=models.SET_DEFAULT,default=1)
    Shipping_status  = models.CharField(
        max_length=5,
        choices=status_choices,
        default=SHIPPING,
    )
    created_at = models.DateTimeField(default=now)
