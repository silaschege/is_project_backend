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

                    previousProduct= ProductsModel.objects.filter(id=product_id)
                    addedProductQuantity = previousProduct.quantity  + differeneceQuantity

                    ProductsModel.objects.filter(id=product_id).update(
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

                    previousProduct= ProductsModel.objects.filter(id=product_id)
                    decreaseProductQuantity = previousProduct.quantity  - differeneceQuantity

                    ProductsModel.objects.filter(id=product_id).update(
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
                        product = ProductsModel.objects.filter(id=product_id)
                        addedProductQuantity = product.quantity  + quantity
                        
                        ProductsModel.objects.filter(id=product_id).update(
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


# add instalment Holder
# holds primary key of items added to Installment
# calculate total
installmentHolderList = []

def FarmerAddInstallmentHolder(request,product_id):
    installmentHolderList.append(product_id)
    product= ProductsModel.objects.get(pk=product_id)
    print('Cart List:',installmentHolderList)
    Cart.objects.create(product_id=product,user=request.user)


    messages.info(request, ('Item added to cart '))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def farmerCart(request):
    form = FarmerShippingDateForm(request.POST, request.FILES)
    if request.method == "POST":
        form = FarmerShippingDateForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save

    product = Cart.objects.filter(user=request.user)
    allcartProducts = []
    total=[]
    for p in product:
        item=ProductsModel.objects.get(pk=p.product_id)
        total.append(item.productPrice)
        allcartProducts.append(item)
    allcartProducts  
  
#    calculate totals
    alltotals= sum(total)
    
    print(allcartProducts)
    return render(request,'installmentFarmer/cart.html',{'allcartProducts':allcartProducts,'alltotals':alltotals,'form':form})

def farmerCartRemove(request,product_id):
    cart=Cart.objects.filter(product_id=product_id).filter(user=request.user)
    print(cart)
    cart.delete()
    messages.info(request, ('Item removed from cart '))
    return render(request,'installmentFarmer/cart.html',{})

# add Installment
def createInstallmentHolder(request,alltotals):
    form = FarmerShippingDateForm(request.POST,request.FILES)
    user=request.user
    if form.is_valid():
            installment = form.save(commit=False)
            installment.user_id=user
            installment.total_amount= alltotals
            installment.save()
  
    InstallmentNumber = InstallmentNumberModel.objects.filter(user_id=user).order_by('created_at').last()
    cart=Cart.objects.filter(user=user)

    products = ProductsModel.objects.filter(id=cart)
 

    # create installment model
    InstallmentModel.objects.create(installmentNumber=InstallmentNumber,product_id=products,quantity=1)
    messages.info(request, ('Installment Created '))
    return render(request,'Farmerproducts/FarmerInstallmentList.html',{})

    
    


    
# filter using the primary key saved in the add installmentholder model
# create the installment number first then use last created to filter the latest one 
# use the installment holder number to add installment item table and reduce the quantity from product table

# farmersee intallment list
# see installments by installment number in the table and pay
# then create a detail view to see each installment and update or remove

# manufacturersee Installment
# see install ments and there details and have an admin tempalte using charts to see installments

