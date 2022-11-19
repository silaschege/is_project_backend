

from django.shortcuts import render
from finance.forms import FarmerMakePaymentForm

from .models import InstallmentNumberModel,InstallmentModel,Cart,ManufacturerInstallmentRecord
from product.models import ProductsModel
from .forms import FarmerShippingDateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from product.models import ProductsModel
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum


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
    check=Cart.objects.filter(product_id=product).count()
    if check >=1:
        quantity_updated_filter=Cart.objects.filter(product_id=product).filter(user=request.user).first()
        quantity_updated =  quantity_updated_filter.quantity+1
        print(quantity_updated)
        Cart.objects.filter(product_id=product).filter(user=request.user).update(quantity=quantity_updated)
        messages.info(request, ('Item added to cart '))
    elif check<1:
        Cart.objects.create(product_id=product,user=request.user,quantity=1)
        messages.info(request, ('Item added to cart '))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def farmerCart(request):
    form = FarmerShippingDateForm(request.POST, request.FILES)
    if request.method == "POST":
        form = FarmerShippingDateForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save

    product = Cart.objects.filter(user=request.user)
    product_filter = Cart.objects.filter(user=request.user).values('product_id')
    allcartProducts = []
    allcartItemQuantity = []
 
    total=[]
    for p in product_filter:
        item=ProductsModel.objects.get(pk=p['product_id'])
        itemcount = Cart.objects.filter(product_id=p['product_id']).filter(user=request.user)
        total.append(item.productPrice)
        allcartProducts.append(item)
        allcartItemQuantity.append(itemcount)
    allcartProducts 
   
  
#    calculate totals
    alltotals= sum(total)
    
   
    return render(request,'installmentFarmer/cart.html',{'alltotals':alltotals,'form':form,'product':product})


def FarmerCartRemove(request,id):
    cart=Cart.objects.filter(product_id=id).filter(user=request.user)
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
            installment.balance = alltotals
            
            installment.save()
            messages.info(request, ('Shipping date added succesfully'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def FarmerCreateInstallment(request):
    user=request.user
    InstallmentNumber = InstallmentNumberModel.objects.filter(user_id=user).order_by('created_at').last()
  
    cart=Cart.objects.filter(user=user).values('product_id')
    

    for p in cart:
        products = ProductsModel.objects.get(id=p['product_id'])
        Pquantity = Cart.objects.filter(user=user).filter(product_id=products).values('quantity')
        

            
    
        
        for q in Pquantity:
            InstallmentModel.objects.create(installmentNumber=InstallmentNumber,productId=products,quantity=q['quantity'])
            
            
            # creating the holder form mufacturer to be able to know products in the sytem under installmnents 
            check=ManufacturerInstallmentRecord.objects.filter(productId=products).count()
            if check >=1:
                quantity_updated_filter=ManufacturerInstallmentRecord.objects.filter(productId=products).first()
                quantity_updated =  quantity_updated_filter.quantity+q['quantity']
                print(quantity_updated)
                ManufacturerInstallmentRecord.objects.filter(productId=products).update(quantity=quantity_updated)
            
            elif check<1:
                ManufacturerInstallmentRecord.objects.create(productId=products,quantity=q['quantity'])
            
            
        Cart.objects.filter(user=user).filter(product_id=products).delete()
    
    messages.info(request, ('Installment Created '))
    return  render(request,'Farmerproducts/FarmerInstallmentList.html',{})

def FarmerInstallmentDetailView(request,id):
    installments = InstallmentModel.objects.filter(installmentNumber=id)

    return  render(request,'installmentFarmer/installmentDetailView.html',{'installments':installments})

def ManufacturerAllInstallment(request):
    user = request.user
  
    Installments= Installments= ManufacturerInstallmentRecord.objects.filter(productId__productManufacturer=user)

    return  render(request,'installmentManufacturer/all_installments.html',{'Installments':Installments})

def ManufacturerAllInstallmentReport (request):
    user = request.user
    Installments= ManufacturerInstallmentRecord.objects.filter(productId__productManufacturer=user)
    
 
    print(Installments)
            

    
    
    
    return render(request,'installmentManufacturer/manufaturerInstallmentsReport.html',{'Installments':Installments})

    
# filter using the primary key saved in the add installmentholder model
# create the installment number first then use last created to filter the latest one 
# use the installment holder number to add installment item table and reduce the quantity from product table

# farmersee intallment list
# see installments by installment number in the table and pay
# then create a detail view to see each installment and update or remove

# manufacturersee Installment
# see install ments and there details and have an admin tempalte using charts to see installments

