from django import forms
from django.forms import ModelForm
from .models import InstallmentNumberModel

class DateInput(forms.DateInput):
    input_type = 'date'


class FarmerShippingDateForm(ModelForm):
    class Meta:
        model = InstallmentNumberModel
        fields = ('shipping_date',)
        labels={
            'shipping_date':'(YYYY-MM-DD)'
        }
        widget={
            'shipping_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
        }
