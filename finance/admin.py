from django.contrib import admin
from .models import PaymentLogModel,TotalPayment

admin.site.register(PaymentLogModel)
admin.site.register(TotalPayment)



