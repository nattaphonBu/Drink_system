from django.shortcuts import render, get_object_or_404, redirect
from .forms import TypeOfItemFrom, AccountForm ,AuthenticationForm, DrinkingForm,UserChangeForm1
from .models import TypeOfItem, Account, Tea
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from django import template

def add_typeofitem(request):
        if request.method == "POST":
                form = TypeOfItemFrom(request.POST)
                if form.is_valid():
                        name = form.save(commit=False)
                        name.save()
        else:
                form = TypeOfItemFrom()
        return render(request, 'typeofitem_form.html', {'form':form})

def edit_typeofitem(request, id=None):
        item =  get_object_or_404(TypeOfItem, id=id)
        form =TypeOfItemFrom(request.POST or None, instance=item)
        if form.is_valid():
                form.save()
        return render(request,'typeofitem_form.html', {'form': form})
def delete_account(request, id):
        item = get_object_or_404(Account, id=id)
        try:
                if request.method == 'POST':
                        form = AccountForm(request.POST, instance=item)
                        item.delete()
                        messages.success(request, 'You have successfully')
                else:
                        form = AccountForm(instance=item)
        except Exception as e:
                messages.warning(request,'Error {}'.format(e))
        context = {
                'form':form,
                'post': item,
        }
        return redirect("account_list")
        # return render(request,'edit_account.html',context)
def register_account(request):
        if request.method == "POST":
                form = AccountForm(request.POST)
                if form.is_valid():
                        username = form.save(commit=False)
                        username.save()
                        # password = form.save(commit=False)
                        # password.save()
                        # status = form.save(commit=False)
                        # status.save()
                        return redirect("login")
                        
                
        else:
                form = AccountForm()
        return render(request, 'register_form.html', {'form':form})
@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def account_list(request):

        account = Account.objects.all()
        pages = Paginator(account, 5)
        
        page = request.GET.get('page')
        # page_range = paginator.get_page(page)

        # context = {
        #         'items' : pages[0],
        #         'page_range': pages[1],
        # }
        context = {
                "items": account,
                "page_range" : pages,
        }
        return render(request,'account_list.html' ,context)

@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def edit_account(request, id=None):
        template = 'edit_account.html'
        post = get_object_or_404(User, id=id)

        if request.method == "POST":
                form = UserChangeForm1(request.POST, instance=post)

                try:
                        if form.is_valid():
                                form.save()
                                messages.success(request,"Edit Account Success!")
                                return redirect("account_list1")

                except Exception as e:
                        messages.warning(request, 'Error :{}'.format(e))
        else:
                form =UserChangeForm1(instance=post)

        context = {
                'form': form,
                'post': post,
        }
        return render(request,template,context)
        
@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def delete_accounttest(request, id):
        item = get_object_or_404(User, id=id , )
        item.delete()
        messages.success(request, 'Delete Success!!')              
        return redirect("account_list1")

@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def add_Drinking(request):
        if request.method == 'POST':
                form = DrinkingForm(request.POST)
                try:
                        if form.is_valid():
                                tea = form.save(commit=False)
                                tea.save()
                                messages.success(request,"Add Drinking Success!!")
                                return redirect('drink_list')
                except Exception as e:
                        messages.warning(request, 'Error :{}'.format(e))
        else:
                form = DrinkingForm()
        return render(request,"add_drink.html",{'form': form})
@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def edit_Drinking(request, id=None):
        template = 'edit_drink.html'
        post = get_object_or_404(Tea, id=id)

        if request.method == "POST":
                form = DrinkingForm(request.POST, instance=post)

                try:
                        if form.is_valid():
                                form.save()
                                messages.success(request,"Edit Drinking Success!")
                                return redirect("drink_list")

                except Exception as e:
                        messages.warning(request, 'Error :{}'.format(e))
        else:
                form = DrinkingForm(instance=post)

        context = {
                'form': form,
                'post': post,
        }
        return render(request,template,context)
@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def drink_list(request):
        drink = Tea.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(drink, 5)
        try:
                users = paginator.page(page)
        except PageNotAnInteger:
                users = paginator.page(1)
        except EmptyPage:
                users = paginator.page(paginator.num_pages)        
        
                
        context = {
                "items": drink,
                "users" : users,
        }
        return render(request,'drink_list.html' ,context)

@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def delete_drinking(request, id):
        item = get_object_or_404(Tea, id=id , )
        item.delete()
        messages.success(request, 'Delete Success!!')              
        return redirect("drink_list")


def register_account_Auth(request):
        if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Register Success!!')  
                        return redirect("login_view")        
        else:
                messages.success(request, 'Register not Success!!')  
                form = UserCreationForm()
                # return redirect("drink_list")  
        return render(request, 'register_form.html', {'form':form})

# def login_view(request):
#         if request.method == "POST":
#                 form = AuthenticationForm(data=request.POST)
#                 if form.is_valid():  
#                         user = form.get_user()
#                         login(request,user) 
#                         messages.info(request, "ลงชือเข้าใช้สำเร็จ")          
#                         return redirect("drink_list")
#         else:
#                 form = AuthenticationForm()
#         return render(request, 'login1.html',{'form':form})
def login_view(request):
        if request.method == "POST":
                form = AuthenticationForm(data=request.POST)
                if form.is_valid():  
                        user = form.get_user()
                        if user.is_superuser == 1:
                                login(request,user) 
                                messages.info(request, "ลงชือเข้าใช้สำเร็จ")          
                                return redirect("drink_list")
                        else:
                                messages.info(request, "คูณยังไม่ได้รับอนุญาติให้เข้าสู่ระบบ")
        else:
                form = AuthenticationForm()
        return render(request, 'login1.html',{'form':form})

@login_required(login_url='/login1/')
@permission_required('Users.is_superuser')
def account_list1(request):

        account = User.objects.all()
        pages = Paginator(account, 5)
        
        page = request.GET.get('page')
        context = {
                "items": account,
                "page_range" : pages,
        }
        return render(request,'account_list.html' ,context)

def logout_request(request):
        logout(request)
        # messages.info(request, "ลงชื่อออกสำเร็จ")
        return redirect("login_view")
        