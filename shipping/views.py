from django.shortcuts import render
from .models import ShippingRegister
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from installments.models import InstallmentModel, InstallmentNumberModel
from django.contrib import messages
from django.http import HttpResponseRedirect

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



def FarmercurrentShipping(request):
    user = request.user
    currentShipping = ShippingRegister.objects.all().values('installment')
    print(currentShipping)
    installment=[]
    for i in currentShipping:
        insfilter = InstallmentNumberModel.objects.filter(pk=i['installment']).filter(user_id =user).values('id')
        print(insfilter)
        for p in insfilter:
            ins=InstallmentModel.objects.filter(installmentNumber=p['id']).filter(approved=False)
            installment.append(ins)
    installment
    print(installment)
    return render(request,'shippingFarmer/FarmerCurrentShipping.html',{
      'installment':installment
    })

def FarmerReceiveShipping(request):
    user = request.user
    currentShipping = ShippingRegister.objects.all().values('installment')
    print(currentShipping)
    installment=[]
    for i in currentShipping:
        insfilter = InstallmentNumberModel.objects.filter(pk=i['installment']).filter(user_id =user).values('id')
        print(insfilter)
        for p in insfilter:
            ins=InstallmentModel.objects.filter(installmentNumber=p['id']).filter(approved=True).filter(received=False)
            installment.append(ins)
    installment
    print(installment)
    return render(request,'shippingFarmer/FarmerReciveShipping.html',{
      'installment':installment
    })

def FarmerReceiveShipping_Receive(request,id):
    InstallmentModel.objects.filter(installmentNumber=id).update(received=True)
    messages.info(request, ('Shipping item received'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def FarmerShippingHistory(request):
    user = request.user
    currentShipping = ShippingRegister.objects.all().values('installment')
    print(currentShipping)
    installment=[]
    for i in currentShipping:
        insfilter = InstallmentNumberModel.objects.filter(pk=i['installment']).filter(user_id =user).values('id')
        print(insfilter)
        for p in insfilter:
            ins=InstallmentModel.objects.filter(installmentNumber=p['id']).filter(approved=True).filter(received=True)
            installment.append(ins)
    installment

  
    return render(request,'shippingFarmer/FarmerShippingHistory.html',{
      'installment':installment
    })


def ManufacturerShippingApproval(request):
    user = request.user
    shipping = ShippingRegister.objects.filter().values('installment')
    print(shipping)
    installmentShipping=[]
    for i in shipping:
        ins = InstallmentModel.objects.filter(installmentNumber=i['installment']).filter(productId__productManufacturer=user).filter(approved=False)
        installmentShipping.append(ins)
    installmentShipping

    print(installmentShipping)


    
    return render(request,'shippingManufacturer/shippingApproval.html',{
    'installmentShipping':installmentShipping
    })

def ManufacturerShippingApproval_Approval(request,id):
    InstallmentModel.objects.filter(id=id).update(approved=True)
    messages.info(request, ('Shipping item approved'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





    


