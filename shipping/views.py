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
from finance.models import ManufacturerShippingPayment
from product.models import ProductsModel

# Create your views here.
# create a new shipping
# update shipping date
# update shiping status
# receive shipping
# there should be one for retriving shipping


def FarmercurrentShipping(request):
    user = request.user
    currentShipping = ShippingRegister.objects.all().values('installment')
    print(currentShipping)
    installment=[]
    for i in currentShipping:
        insfilter = InstallmentNumberModel.objects.filter(pk=i['installment']).filter(user_id =user).values('id')
        print(insfilter)
        for p in insfilter:
            ins=InstallmentModel.objects.filter(installmentNumber=p['id']).filter(approved=False).filter(approved=False)
            
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
    InstallmentModel.objects.filter(id=id).update(received=True)


    installmentItem = InstallmentModel.objects.filter(id=id).values('productId','quantity')

  

    for i in installmentItem:  
        product = ProductsModel.objects.get(pk=i['productId'])
        print(product)
        sum = product.productPrice * i['quantity']
  
   


    check=ManufacturerShippingPayment.objects.filter(installment=id).count()
    if check >=1:
        quantity_updated_filter=ManufacturerShippingPayment.objects.filter(installment=id).first()
        print(quantity_updated)
        quantity_updated =  quantity_updated_filter.amount + sum
        print(quantity_updated)
        ManufacturerShippingPayment.objects.filter(installment=installmentItem).update(amount=quantity_updated)
        messages.info(request, ('Item added to cart '))
    elif check<1:
        ins = InstallmentModel.objects.get(id=id)
        ManufacturerShippingPayment.objects.create(installment=ins,amount = sum)
        
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

 

    return render(request,'shippingManufacturer/shippingApproval.html',{
    'installmentShipping':installmentShipping
    })

def ManufacturerShippingApproval_Approval(request,id):
    InstallmentModel.objects.filter(id=id).update(approved=True)
    messages.info(request, ('Shipping item approved'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def ManufacturerReceivedShipping(request):
    user = request.user
    shipping = ShippingRegister.objects.filter().values('installment')
    print(shipping)
    installmentShipping=[]
    for i in shipping:
        ins = InstallmentModel.objects.filter(installmentNumber=i['installment']).filter(productId__productManufacturer=user).filter(approved=True).filter(received=True)
        installmentShipping.append(ins)
    installmentShipping



    return render(request,'shippingManufacturer/shippingReceived.html',{
    'installmentShipping':installmentShipping
    })

def AdminShippingProcessing(request):
    installment=InstallmentModel.objects.filter(approved=False).filter(received=False)
    return render(request,'shippingAdmin/adminShippingProcessing.html',{'installment':installment})

def AdminShippingReceived(request):
    installment=InstallmentModel.objects.filter(approved=True).filter(received=True)
    return render(request,'shippingAdmin/adminShippingReceived.html',{'installment':installment})




    


