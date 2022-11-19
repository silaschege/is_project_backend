from django.urls import path
from .views import RegisterUserView,RetrieveUserView,home,Userlogin,Userlogout,FarmerRegistration,ManufacturerRegistration

urlpatterns = [
    path ('register',RegisterUserView.as_view()),
    path ('',home, name="system-home"),
    path ('Userlogin',Userlogin, name="Userlogin"),
    path ('Userlogoutn',Userlogout, name="Userlogout"),
    path ('FarmerRegistration',FarmerRegistration, name="FarmerRegistration"),
    path ('ManufacturerRegistration',ManufacturerRegistration, name="ManufacturerRegistration"),
    
 
  

]