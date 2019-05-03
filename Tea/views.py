from django.shortcuts import render, get_object_or_404
from .forms import TypeOfItemFrom, AccountForm
from .models import TypeOfItem, Account
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
def delete_post(request, pk):
        item = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
                form = TypeOfItemFrom(request.POST, instance=item)
                item.delete()
                message.success(request, 'You have successfully')
        else:
                form = TypeOfItemFrom(instance=post)
        context = {
                'form':form
        }

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

        # context = {
        #         'items' : pages[0],
        #         'page_range': pages[1],
        # }
        context = {
                "items": account,
                "title" : "page"
        }
        return render(request,'account_list.html' ,context)