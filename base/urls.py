from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^orderbase/', 'orderapp.views.orderbase', name='orderbase'),
    url(r'^empbase/', 'empapp.views.empbase', name='empbase'),
    url(r'^custlogin/', 'orderapp.views.custlogin', name='custlogin'),
    url(r'^createacct/', 'orderapp.views.createacct', name='createacct'),

    url(r'^admin/', include(admin.site.urls)),


)