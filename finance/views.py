from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import PaymentLogModel
from installments.models import InstallmentModel,InstallmentNumberModel
from .forms import FarmerMakePaymentForm
from django.contrib import messages
from product.models import ProductsModel

# Create your views here.

# record payment with installment 
# check if order if blance is zero and make balance into zero
# balance is difference of total sum of installments minus the total amount paid 
# total amount paid is total amount paid plus previous total amount paid 
# change installment stattus to paid if balance is zero
# balance is zero then it is moved to shipping

# there should be a get model for getting all payment logs for each user
# total paid and balance will beused by manufacturers when thet are doing manufacturing reports


# the total paid amount and balance  is calculated befor being created
# check if balance is zero and create the shipping and also if its zero before to deny payment
class MakePayment(APIView):
    def post(self,request):
        try:
            data = request.data
            user = request.user

            
            installment_id = data['installment_id']
            amount  = data['amount']

            paymentMethod = data['paymentMethod']

            previousPayments = PaymentLogModel.objects.all(installment_id=installment_id)
            previousPaymentCount = PaymentLogModel.objects.all(installment_id=installment_id)
            installmentPrice = InstallmentModel.objects.filter(installment_id=installment_id)
            

            if user.is_famer == True:
                for x in previousPaymentCount:
                    totalPaid = totalPaid+previousPayments.amount
                    return totalPaid
                
                totalAmountPaid = totalPaid + amount
                balance = installmentPrice.total_amount - totalAmountPaid

                PaymentLogModel.objects.create(
                    user_id = user,
                    amount =amount,
                    totalAmountPaid  = totalAmountPaid,
                    balance = balance,
                    paymentMethod = paymentMethod

                )

                return Response(
                    {'Success':'Payment succesfully done'},
                    status= status.HTTP_201_CREATED
                )

            
            else:
                return Response (
                    {'Error':'You do not have permission to complete this operation'},
                    status = status.HTTP_400_BAD_REQUEST
                )




        except:
            return Response(
                {'Error':'Internal server error when making payment'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def farmerMakePayment(request,id):
    
    form = FarmerMakePaymentForm(request.POST, request.FILES)
    if request.method == "POST":
        form = FarmerMakePaymentForm(request.POST, request.FILES)
        ins = InstallmentNumberModel.objects.get(pk=id)
    
        if form.is_valid():
           payment=form.save(commit=False)
           payment.installment_id = ins
           payment.user_id = request.user
           payment.save()
           messages.success(request, ("Your installment has been paid for"))

    return render(request,'farmer/farmerMakePayment.html',{'form':form})

def farmerPaymentHistory(request):
    user =request.user
    payment = PaymentLogModel.objects.filter(user_id = user )
    return render(request,'farmer/farmerPaymentHistory.html',{'payment':payment})

def ManufacturerPaymentHistory(request):
    user = request.user 
    installment= InstallmentModel.objects.filter(productId__productManufacturer=user).values('installmentNumber_id').order_by('installmentNumber_id').distinct()
    print(installment)
    payment = []
    for i in installment:
        try:
            pay = PaymentLogModel.objects.get(installment_id = i['installmentNumber_id'])
            payment.append(pay)
            print(pay)
        except PaymentLogModel.DoesNotExist:
            pay = None

    payment

    return render(request,'manufacturer/manufacturerPaymentHistory.html',{'payment':payment})
