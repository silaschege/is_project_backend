from dataclasses import fields
from urllib import request
from django import forms
from django.forms import ModelForm
from .models import PaymentLogModel
from installments.models import InstallmentNumberModel

class FarmerMakePaymentForm(ModelForm):
    class Meta:
        model=PaymentLogModel
        fields=('amount',)
        labels={
                
                'amount':'amount'
        }
        widgets={
            'amount': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Amount'}),
        }
