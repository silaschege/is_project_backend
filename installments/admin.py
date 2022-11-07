from django.contrib import admin
from .models import InstallmentModel,InstallmentNumberModel,Cart

admin.site.register(InstallmentModel)
admin.site.register(InstallmentNumberModel)
admin.site.register(Cart)