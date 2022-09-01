from django.contrib.auth import get_user_model
User = get_user_model()
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

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

