from django.db import models
from installments.models import InstallmentModel
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
    installment = models.ManyToManyField(InstallmentModel)
    Shipping_status  = models.CharField(
        max_length=5,
        choices=status_choices,
        default=SHIPPING,
    )
    created_at = models.DateTimeField(default=now)
