from django.contrib import admin
from .models import ProductCategoryModel,ProductModel,ProductNameModel

admin.site.register(ProductCategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProductNameModel)
