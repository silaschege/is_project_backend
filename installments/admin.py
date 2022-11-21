from django.contrib import admin
from .models import InstallmentModel,InstallmentNumberModel,Cart,ManufacturerInstallmentRecord

admin.site.register(InstallmentModel)
admin.site.register(InstallmentNumberModel)
admin.site.register(Cart)
admin.site.register(ManufacturerInstallmentRecord)