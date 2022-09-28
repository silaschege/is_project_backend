from django.contrib import admin
from .models import InstallmentModel,InstallmentNumberModel

admin.site.register(InstallmentModel)
admin.site.register(InstallmentNumberModel)
