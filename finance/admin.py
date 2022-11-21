from django.contrib import admin
from .models import PaymentLogModel,TotalPayment,ManufacturerShippingPayment

admin.site.register(PaymentLogModel)
admin.site.register(TotalPayment)
admin.site.register(ManufacturerShippingPayment)


