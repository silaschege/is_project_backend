from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model 
User = get_user_model()
from manufacturer.models import ManufactureRegisterModel
from .models import ProductModel
from .serializer import ProductModelSerializer

# Create your views here.


# get a the foreign key id and then connect them for manufacturer because there is a ratio of many is to
# get foreign key but the manufacturer has one foreign key for admin purposes but thereis a sub table for the relationships this is a future plan


# add a product
# update a product dlete a product
# when a customer makes an installment the product quantity is reduce and when the installment is not complete there is a role back to the products table


# add product and shuld be manufacturer
class RetrieveProductsManufacturer(APIView):
    def get(self,request,format=None):
        try:
            user = request.User
            if user.is_manufacture==True:
                manufacturer_filter = ManufactureRegisterModel.objects.filter(user = user)
                
                products =ProductModel.objects.get(
                    manufacturer = manufacturer_filter
                )

                product_serialized =ProductModelSerializer(products,many=True)

                return Response(
                    {'ManufacturerProducts':product_serialized.data},
                    status= status.HTTP_200_OK
                )
            
            else:
                return  Response(
                            {'Error':'You do not have the permision to make any changes'},
                            status= status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'Error':'Something went wrong when retreiving products'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR    
            )

class RetrieveProductFarmer(APIView):
    def get(self,request,format=None):
        try:
            user = User.request
        
            if user.is_farmer ==True:
                products =ProductModel.objects.get()
                product_serialized =ProductModelSerializer(products,many=True)
                return Response(
                        {'ManufacturerProducts':product_serialized.data},
                    status= status.HTTP_200_OK
                    )
        
            else:
                return Response(
                    {'Error':'You do not have permisssion to view this'},
                    status= status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                    {'Error':'Something went wrong when retreiving products'},
                    status= status.HTTP_500_INTERNAL_SERVER_ERROR    
                )

class AddNewProductManufacturer(APIView):
    def post (self,request):
        try:
            user = request.User
            data =request.data

            productName = data['productName ']
            productCategory = data['productCategory']
            price = data['price']
            quantity = data['quantity']
            packagingQuantity = data['packagingQuantity']
            product_image = data['product_image']

            if ManufactureRegisterModel.objects.filter(user = user).exists():
                if user.is_manufacture==True:
                    manufacturer_filter = ManufactureRegisterModel.objects.filter(user = user)
                    
                    ProductModel.objects.create(          
                        productName = productName,
                        productCategory = productCategory,
                        manufacturer = manufacturer_filter,
                        price = price,
                        quantity = quantity,
                        packagingQuantity = packagingQuantity,
                        product_image = product_image,
                    )

                    return Response(
                        {'Success':'Product added succesfully'},
                        status= status.HTTP_201
                    )

                else:
                    return  Response(
                            {'Error':'You do not have the permision to make any changes'},
                            status= status.HTTP_400_BAD_REQUEST
                        )
            
            else:
                 return  Response(
                            {'Error':'Manufacturer does not exist'},
                            status= status.HTTP_400_BAD_REQUEST
                        )
        except:
            return Response(
                {'Error':'Something went wrong when adding products'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                
            )





# delete product and should be a manufaturer
class DeleteProduct(APIView):
    def delete (self,request):
        user = User.request
        data = request.data
        id = data['id']
        try:
            if user.is_manufacture==True:

                if not ProductModel.objects.filter(id=id).exists():
                    return Response (
                        {'Error':'Product does not exist'},
                        status= status.HTTP_404_NOT_FOUND
                    )
                
                ProductModel.objects.filter(id=id).delete()

                if not ProductModel.objects.filter(id=id).exists():
                    return Response(
                        {'Success':'Product deleted successfully'},
                        status= status.HTTP_204_NO_CONTENT
                    )

                else:
                    return Response (
                        {'Error':'Failed to delete product'},
                        status= status.HTTP_400_BAD_REQUEST
                    )

            
            else:
                return Response(
                {'Error':'You do not have permisssion to conduct the operation being attempted'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except:
            return Response(
                {'Error':'Something went wrong when deleting products'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )
               



