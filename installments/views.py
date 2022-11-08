from django.db.models import Q

from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import InstallmentNumberModel,InstallmentModel,Cart
from product.models import ProductsModel
from .forms import FarmerShippingDateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from product.models import ProductsModel
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponseRedirect


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
# there should be a listener that when an installment is deleted it notifies the manufacturer and also if 
# any money was paid the money minus some sum moves into the wallet
# deletes and also updates the product table
# add instalment Holder
# holds primary key of items added to Installment
# calculate total
installmentHolderList = []

def FarmerAddInstallmentHolder(request,product_id):
    installmentHolderList.append(product_id)
    product= ProductsModel.objects.get(pk=product_id)
    Cart.objects.create(product_id=product,user=request.user)
    messages.info(request, ('Item added to cart '))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def farmerCart(request):
    form = FarmerShippingDateForm(request.POST, request.FILES)
    if request.method == "POST":
        form = FarmerShippingDateForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save

    product = Cart.objects.filter(user=request.user).values('product_id')
    allcartProducts = []
 
    total=[]
    for p in product:
        item=ProductsModel.objects.get(pk=p['product_id'])
        total.append(item.productPrice)
        allcartProducts.append(item)
    allcartProducts  
  
#    calculate totals
    alltotals= sum(total)
    
   
    return render(request,'installmentFarmer/cart.html',{'allcartProducts':allcartProducts,'alltotals':alltotals,'form':form})


def farmerCartRemove(request,product_id):
    cart=Cart.objects.filter(product_id=product_id).filter(user=request.user)
    cart.delete()
    messages.info(request, ('Item removed from cart '))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# add Installment
def farmerCreateInstallmentNumber(request,alltotals):
    user=request.user
    if request.method == "POST":
        form = FarmerShippingDateForm(request.POST,request.FILES)
        if form.is_valid():
            installment = form.save(commit=False)
            installment.user_id=user
            installment.total_amount= alltotals
            print(installment)
            installment.save()
            messages.info(request, ('Shipping date added succesfully'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def FarmerCreateInstallment(request):
    user=request.user
    InstallmentNumber = InstallmentNumberModel.objects.filter(user_id=user).order_by('created_at').last()
    print('Installment number:',InstallmentNumber)
    cart=Cart.objects.filter(user=user).values('product_id')
    print('cart:',cart)
    for p in cart:
        products = ProductsModel.objects.get(id=p['product_id'])
        InstallmentModel.objects.create(installmentNumber=InstallmentNumber,product_id=products,quantity=1)
        print('products:',products)
    
    messages.info(request, ('Installment Created '))
    return  render(request,'Farmerproducts/FarmerInstallmentList.html',{})

def FarmerInstallmentDetailView(request,id):
    installmentNO = InstallmentNumberModel.objects.filter(id=id)
    print(installmentNO)
    installments = InstallmentModel.objects.filter(installmentNumber=installmentNO)
  
    print(installments)
    return  render(request,'installmentFarmer/installmentDetailView.html',{'installments':installments})
    


    
# filter using the primary key saved in the add installmentholder model
# create the installment number first then use last created to filter the latest one 
# use the installment holder number to add installment item table and reduce the quantity from product table

# farmersee intallment list
# see installments by installment number in the table and pay
# then create a detail view to see each installment and update or remove

# manufacturersee Installment
# see install ments and there details and have an admin tempalte using charts to see installments

