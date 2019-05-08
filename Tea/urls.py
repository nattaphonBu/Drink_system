from django.conf.urls import url
from . import views
# from .views

urlpatterns = [
    url(r'^add/typeofitem/$', views.add_typeofitem, name='add_typeofitem'),
    url(r'^edit/typeofitem/(?P<id>\d+)/$', views.edit_typeofitem, name='edit_typeofitem'),
    url(r'^register/$', views.register_account , name='register_account'),
    url(r'^account/$', views.account_list, name='account_list'),
    # url(r'^delete_acount/(?P<id>\d+)/$', views.delete_post, name='delete_post_Account')
    url(r'^account/edit/(?P<id>\d+)/$', views.edit_account, name='edit_account'),
    url(r'^account/(?P<id>\d+)/delete', views.delete_accounttest, name='delete_account'),
]

