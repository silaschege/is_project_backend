from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)





urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('user/',include('user.urls'),name='user_urls'),
    path('manufacturer/',include('manufacturer.urls'),name='manufacturer'),
    path('product/',include('product.urls'),name='product'),
    path('installment/',include('installments.urls'),name='product'),
    path ('finance/',include('finance.urls'),name='finance'),
    path('shipping/',include('shipping.urls'),name='shipping'),
    path('admin/', admin.site.urls),
    
    # path ('/finance' ,include(finance_router.urls,'finance')),

 
]


