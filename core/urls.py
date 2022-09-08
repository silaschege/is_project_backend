from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from finance.routes import finance_router
from installments.routes import installments_router
from land.routes import land_router
from manufacturer.routes import  manufacturer_router
from product.routes import products_router

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('user/',include('user.urls'),name='user_urls'),
    path('admin/', admin.site.urls),
    path ('/finance' ,include(finance_router.urls,'finance')),
    path ('/installment' ,include(installments_router.urls,'installments')),
    path ('/land' ,include(land_router.urls,'land')),
    path ('/manufacturer',include(manufacturer_router.urls,'manufacturer')),
    path ('/product',include(products_router.urls,'product')),
]


