from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import PaymentLogModel,TotalPayment,ManufacturerShippingPayment
from installments.models import InstallmentModel,InstallmentNumberModel
from .forms import FarmerMakePaymentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Sum

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
def farmerMakePayment(request,id):
    user = request.user
    form = FarmerMakePaymentForm(request.POST, request.FILES)
    if request.method == "POST":
        form = FarmerMakePaymentForm(request.POST, request.FILES)
        ins = InstallmentNumberModel.objects.get(pk=id)
    
        if form.is_valid():
           amount = form.cleaned_data['amount']
           fetchbalance=InstallmentNumberModel.objects.get(pk=id)
           fetchbalance.balance=fetchbalance.balance - amount
           fetchbalance.save()
           payment=form.save(commit=False)
           payment.installment_id = ins
           payment.user_id = user
           payment.save()
           check=TotalPayment.objects.filter(installment_id=id).filter(user_id=user).count()
           if check >=1:
                quantity_updated_filter=TotalPayment.objects.filter(installment_id=id).filter(user_id=user).first()
                updatedamount =  quantity_updated_filter.amount+form.cleaned_data.get('amount')
                print(amount)
                messages.success(request, ("Your installment has been paid for"))
                TotalPayment.objects.filter(installment_id=id).filter(user_id=user).update(amount=updatedamount)
           elif check<1:
                installment = InstallmentNumberModel.objects.get(pk=id)
                TotalPayment.objects.create(installment_id=installment,user_id=request.user,amount=form.cleaned_data.get('amount'))
                messages.success(request, ("Your installment has been paid for"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    
    return render(request,'financefarmer/farmerMakePayment.html',{'form':form})

def farmerPaymentHistory(request):
    user =request.user
    payment = PaymentLogModel.objects.filter(user_id = user )
    return render(request,'financefarmer/farmerPaymentHistory.html',{'payment':payment})

def farmerAllPayment(request):
    user =request.user
    payment =TotalPayment.objects.filter(user_id = user )
    return render(request,'financefarmer/farmerAllPayment.html',{'payment':payment})

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

def ManufacturerShippingpayment(request):
    user= request.user
    items=ManufacturerShippingPayment.objects.filter(installment__productId__productManufacturer=user)
    total=ManufacturerShippingPayment.objects.filter(installment__productId__productManufacturer=user).aggregate(Sum('amount'))
    print(total)
    
    print(items)
    return render(request,'manufacturer/manufacturerShippingPayment.html',{'items':items,'total':total})

