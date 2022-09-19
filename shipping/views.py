from datetime import date
from hashlib import sha512
from django.shortcuts import render
from .models import ShippingRegister
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from installments.models import InstallmentModel

# Create your views here.
# create a new shipping
# update shipping date
# update shiping status
# receive shipping
# there should be one for retriving shipping

class CreateShippingView(APIView):
    def post(self,request):
        try:
            data = request.data

            installment = data['insallment_id']
            Shipping_status  = data['Shipping_status']

            if not InstallmentModel.objects.filter(id=installment).exists():
                return Response(
                {'Error':'Installment does not exist'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            ShippingRegister.objects.create(
                installment = installment,
                Shipping_status = Shipping_status

            )

                
            
        except:
            return Response(
                {'Error':'Error occured when trying to create shipping'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateShipping(APIView):
    def put(self,request):
        try:
            data = request.data

            id = data['id']
            Shipping_status  = data['Shipping_status']

            if not ShippingRegister.objects.filter(id= id).exists():
                return Response(
                {'Error':'Shipping does not exist'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            ShippingRegister.objects.filter(id=id).update(
                Shipping_status = Shipping_status
            )

            
        except:
            return Response(
                {'Error':'Error occured when trying to update shipping'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )




