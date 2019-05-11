from django.forms import ModelForm
from .models import TypeOfItem, Account , Tea
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class TypeOfItemFrom(ModelForm):
    # your_name = forms.CharField(label='Your Name',max_length = 100)
    class Meta:
        model = TypeOfItem
        fields = ['name', 'description']
    

class AccountForm(ModelForm):
    class Meta:
        model = Account
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        } 
        fields = ['username','password','name','tell','status_account']

class AuthenticationForm(ModelForm):
    class Meta:
        model = Account
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        } 
        fields = ['username','password']

class DrinkingForm(ModelForm):
    drinkname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5 center',
        }
    ))
    price = forms.FloatField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5 center',
        }
    ))
    class Meta:
        model = Tea
        fields = ['drinkname','price']

# class RegiserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['status']
        
class UserChangeForm1(ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5 center',
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5',
        }
    ))
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)
