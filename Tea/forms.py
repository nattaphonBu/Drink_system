from django.forms import ModelForm
from .models import TypeOfItem, Account


class TypeOfItemFrom(ModelForm):
    # your_name = forms.CharField(label='Your Name',max_length = 100)
    class Meta:
        model = TypeOfItem
        fields = ['name', 'description']
    

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username','password','status','status_account']
