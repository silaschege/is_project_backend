from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('',include('user.urls'),name='user_urls'),
    # user authentication system being refrenced and bundled up
    path('',include('django.contrib.auth.urls')),
    path('manufacturer/',include('manufacturer.urls'),name='manufacturer'),
    path('product/',include('product.urls'),name='product'),
    path('installment/',include('installments.urls'),name='installment'),
    path ('finance/',include('finance.urls'),name='finance'),
    path('shipping/',include('shipping.urls'),name='shipping'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


