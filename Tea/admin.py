from django.contrib import admin
from .models import TypeOfItem, Account, Tea
# Register your models here.


admin.site.register(TypeOfItem)
admin.site.register(Account)
admin.site.register(Tea)