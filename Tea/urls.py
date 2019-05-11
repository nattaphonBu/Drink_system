from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


# from .views

urlpatterns = [
    url(r'^add/typeofitem/$', views.add_typeofitem, name='add_typeofitem'),
    url(r'^edit/typeofitem/(?P<id>\d+)/$', views.edit_typeofitem, name='edit_typeofitem'),
    url(r'^register/$', views.register_account , name='register_account'),
    # url(r'^account/$', views.account_list, name='account_list'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^login1/$', views.login_view, name='login_view'),
    # url(r'^delete_acount/(?P<id>\d+)/$', views.delete_post, name='delete_post_Account')
    url(r'^account/edit/(?P<id>\d+)/$', views.edit_account, name='edit_account'),
    url(r'^account/(?P<id>\d+)/delete', views.delete_accounttest, name='delete_account'),
    url(r'^add_drink/$', views.add_Drinking, name='add_Drinking'),
    url(r'^drink/edit/(?P<id>\d+)/$', views.edit_Drinking, name='edit_Drinking'),
    url(r'^drink/$', views.drink_list, name='drink_list'),
    url(r'^drink/(?P<id>\d+)/delete', views.delete_drinking, name='delete_drinking'),
    url(r'^register_auth/$', views.register_account_Auth, name='register_account_Auth'),
     url(r'^account/$', views.account_list1, name='account_list1'),
    url(r'^logout/$', views.logout_request, name='logout_request'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)