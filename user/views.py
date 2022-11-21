from cgitb import html
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages




# Create your views here.
class RegisterUserView(APIView):
    
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        try:
            data= request.data
            
            email = data['email']
            email = email.lower()
            name = data['name']
            password=data['password']
            re_password= data['re_password']
            is_farmer = data['is_farmer']
            is_delivery = data['is_delivery']
            is_manufacture = data['is_manufacturer']

            if is_farmer == 'True':
                is_farmer = True
            else:
                is_farmer = False
            
            if is_delivery == 'True':
                is_delivery = True
            else:
                 is_delivery = False

            if is_manufacture == 'True':
                is_manufacture = True
            else:
                is_manufacture = False

            if password == re_password:
                if len(password)>=8:
                    if not User.objects.filter(email=email).exists():
                        if is_farmer==True:
                            User.objects.create_farmer(email=email,name=name,password=password)

                            return  Response(
                                {'Success':'Farmer created successfully'},
                                status= status.HTTP_201_CREATED
                            )
                        
                        if is_delivery==True:
                            User.objects.create_delivery(email=email,name=name,password=password)

                            return  Response(
                                {'Success':'Delivery created successfully'},
                                status= status.HTTP_201_CREATED
                            )
                        
                        if is_manufacture==True:
                            User.objects.create_manufacturer(email=email,name=name,password=password)

                            return  Response(
                                {'Success':'Manufacturer created successfully'},
                                status= status.HTTP_201_CREATED
                            )
                    
                    else:
                        return  Response(
                            {'Error':'User with this email already exists'},
                            status= status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return  Response(
                        {'Error':'Password must be atlleast 8 characters'},
                        status= status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'Error':'Passwords do not match'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'Error':'Something went wrong when registering an account'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                
            )
                
               
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user 
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'Error':'Something went wrong when reetrieving data'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def home (request):
    return render(request,'users/home.html',{})

def Userlogin (request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        # login the user
        if user is not None:

            login(request,user)
            # check what the user flag is
            user = request.user 
            if user.is_staff==True:
                return redirect('AdminAddCategoryU')

            if user.is_farmer==True:
                return redirect('FarmerInstallmentListView')
            
            if user.is_manufacturer==True:
                return redirect('ManufacturerStore')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('Userlogin')	
    else:
        return render(request,'users/login.html',{})


def Userlogout(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('system-home')

def FarmerRegistration(request):
    
    return render(request,'users/FarmerRegister.html',{})

def ManufacturerRegistration(request):
  
    return render(request,'users/ManufacturerRegister.html',{})
   