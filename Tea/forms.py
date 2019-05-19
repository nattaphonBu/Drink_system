from django.forms import ModelForm
from .models import TypeOfItem, Account , Tea
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class AuthenticationForm(ModelForm):
    class Meta:
        model = Account
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        } 
        fields = ['username','password']

class DrinkingForm(ModelForm):
    drinkname = forms.CharField(required=False,label= "Material Name",widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5 center required',
            'placeholder': 'ชื่อเครื่องดื่ม'
        }
    ))
    price = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class' : 'form-control col-5 center required',
            'placeholder': 'ราคา'
        }
    ))
    class Meta:
        model = Tea
        fields = ['drinkname','price']
    
class TypeOfItemFrom(ModelForm):
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
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5',
        }
    ))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class UserChangeForm2(ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control col-5 center',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control col-5 center',
        }
    ))

    class Meta:
        model = User
        fields = ('username','password',)