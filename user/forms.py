from django import forms
from django.forms import ModelForm
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class FarmerRegistation(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Your email is required ',widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserAccount
        fields = ('email','name')
    
    def __init__(self, *args, **kwargs):
        super(FarmerRegistation,self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    

