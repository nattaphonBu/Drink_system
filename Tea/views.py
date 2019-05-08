from django.shortcuts import render, get_object_or_404, redirect
from .forms import TypeOfItemFrom, AccountForm
from .models import TypeOfItem, Account
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView


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
                        
                
        else:
                form = AccountForm()
        return render(request, 'register_form.html', {'form':form})

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

# def delete_post_Account(request, id):
#         account = AccountForm(request.POST)
#         if request.method == 'POST':
#                 form = AccountForm(request.POST, instance=account)
#                 account.delete()
#                 messages.success(request,'You have successfully')
#         else:
#                 account = AccountForm(instance=account)
#         context = {
#                 'form': form,
#                 'account': account,
#         }
#         return render(request,'account_list.html' ,context)

def edit_account(request, id=None):
        template = 'edit_account.html'
        post = get_object_or_404(Account, id=id)

        if request.method == "POST":
                form = AccountForm(request.POST, instance=post)

                try:
                        if form.is_valid():
                                form.save()
                                messages.success(request,"success")

                except Exception as e:
                        messages.warning(request, 'Error :{}'.format(e))
        else:
                form =AccountForm(instance=post)

        context = {
                'form': form,
                'post': post,
        }
        return render(request,template,context)

def delete_accounttest(request, id):
        item = get_object_or_404(Account, id=id)
        item.delete()
                      
        return redirect("account_list")

