from django.contrib import admin
from .models import ProductCategoryModel,ProductNameModel,PackagingMetric,PackagingQuantity,ProductsModel

admin.site.register(ProductCategoryModel)
admin.site.register(ProductNameModel)
admin.site.register(PackagingMetric)
admin.site.register(PackagingQuantity)
admin.site.register(ProductsModel)
