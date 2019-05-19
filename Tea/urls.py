from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/$', views.register_account , name='register_account'),
    url(r'^login1/$', views.login_view, name='login_view'),
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