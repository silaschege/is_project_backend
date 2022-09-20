from asyncio import run_coroutine_threadsafe
from statistics import quantiles
from django.shortcuts import render
from rest_framework.views import APIView
from .models import InstallmentModel
from django.contrib.auth import get_user_model
User = get_user_model()
from product.models import ProductModel
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# update installment
# remove installment
# calculating total and storing it 

# add installment and decrease product quantity
# calculae totalinstallments

# automatically deduct the quatity of the product when installm,
# and is added and vice verse when its deleted or not paid in time
# create installment 
# total amount of installment price will be callculted int the frontend
class AddInstallments(APIView):
    def post(self,request):
        data = request.data
        user = request.user

      

        product_id = data['id']
        quantity = data['quantity']
        shipping_date = data['shipping_date']
        total_amount = data['total_amount']
 

        

        product = ProductModel.objects.filter(id=product_id)
        
    
        if user.is_farmer == True:
            newQuantity=product.quantity-quantity

            InstallmentModel.objects.create(
                    product_id = product_id,
                    quantity = quantity,
                    shipping_date = shipping_date,
                    total_amount = total_amount,
                    user_id = user
            )

            if not ProductModel.objects.filter(id=product).exists():
                return Response (
                    {'ERROR':'PRODUCT DOES NOT EXIST'},
                    status= status.HTTP_404_NOT_FOUND
                )
            
            ProductModel.objects.filter(id=product_id).update(
                quantity = newQuantity
            )

            return Response (
                {'SUCCESS':'Installment succesfuly created'},
                status= status.HTTP_201_CREATED
            )
            
            
        
        else:
            return Response(
                {'ERROR':'You do not have the permission to perform this action'},
                status= status.HTTP_400_BAD_REQUEST
            )


class UpdateInstallmentQuantity(APIView):
    # new total amoutn will be updated from frontend
    def put(self,request):
        try:
            data = request.data
            user = request.user

        

            installment_id = data['id']
            product_id = data['product_id']
            newQuantity = data ['newQuantity']
            total_amount = data['total_amount']

            previousInstallment = InstallmentModel.objects.filter(id=installment_id)
            differeneceQuantity = previousInstallment.quantity - newQuantity
            
            

            if user.is_farmer == True:
                if not InstallmentModel.objects.filter(id=installment_id).exists():
                    return Response(
                        {'ERROR':'Installment does not exist'},
                        status= status.HTTP_404_NOT_FOUND
                    )
                
                if previousInstallment.quantity>=newQuantity:
                    InstallmentModel.objects.filter(id=installment_id).update(
                        quantity = newQuantity,
                        total_amount =total_amount
                    )

                    previousProduct= ProductModel.objects.filter(id=product_id)
                    addedProductQuantity = previousProduct.quantity  + differeneceQuantity

                    ProductModel.objects.filter(id=product_id).update(
                        quantity = addedProductQuantity
                    )

                    return Response (
                        {'SUCCESS':'Installment change success fully'},
                        status= status.HTTP_200_OK
                    )

                    
                if previousInstallment.quantity<=newQuantity:
                    InstallmentModel.objects.filter(id=installment_id).update(
                        quantity = newQuantity,
                        total_amount =total_amount
                    )

                    previousProduct= ProductModel.objects.filter(id=product_id)
                    decreaseProductQuantity = previousProduct.quantity  - differeneceQuantity

                    ProductModel.objects.filter(id=product_id).update(
                        quantity = addedProductQuantity
                    )

                    return Response (
                        {'SUCCESS':'Installment change  success fully'},
                        status= status.HTTP_200_OK
                    )
                    

            
            else:
                return Response(
                    {'ERROR':'You do not have the permission to perform this action'},
                    status= status.HTTP_400_BAD_REQUEST
                    )


        
        except:
            return Response(
                 {'ERROR':'Internal server error'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# there should be a listener that when an installment is deleted it notifies the manufacturer and also if 
# any money was paid the money minus some sum moves into the wallet
# deletes and also updates the product table
class RemoveInstallment(APIView):
    def delete(self,request):
        try:
            data = request.data
            user = request.user
            installment_id = data['id']
            user_id = data['user_id']
            quantity = data['quantity']
            product_id = data['product_id']

            if user.is_farmer == True:
                if user.id == user_id:
                    if not InstallmentModel.objects.filter(id=installment_id).exists():
                        return Response (
                            {'ERROR':'Installment does not exist'},
                            status= status.HTTP_404_NOT_FOUND
                        )
                    
                    if quantity>=1:
                        product = ProductModel.objects.filter(id=product_id)
                        addedProductQuantity = product.quantity  + quantity
                        
                        ProductModel.objects.filter(id=product_id).update(
                        quantity = addedProductQuantity
                        )
                    
                    InstallmentModel.objects.filter(id=installment_id).delete()

                    if not InstallmentModel.objects.filter(id=installment_id).exists():
                        return Response(
                            {'SUCCESS':'Installment deleted successfully'},
                            status= status.HTTP_204_NO_CONTENT
                        )

                    else:
                        return Response(
                            {'ERROR':'Installment failed to delete'},
                            status= status.HTTP_400_BAD_REQUEST
                        )





                

                else:
                    return Response(
                        {'ERROR':'You do not have the permission to perform this action'},
                        status= status.HTTP_400_BAD_REQUEST
                    )

            
            else:
                return Response(
                    {'ERROR':'You do not have the permission to perform this action'},
                    status= status.HTTP_400_BAD_REQUEST
                    )


        
        except:
            return Response(
                 {'ERROR':'Internal server error'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )



