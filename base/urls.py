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
    url(r'^delivery/', 'orderapp.views.delivery', name='delivery'),
    url(r'^carryout/', 'orderapp.views.carryout', name='carryout'),
    url(r'^delorder/', 'orderapp.views.delorder', name='delorder'),
    url(r'^colocation/', 'orderapp.views.colocation', name='colocation'),
    url(r'^coorder/', 'orderapp.views.coorder', name='coorder'),
    url(r'^menu/', 'orderapp.views.menu', name='menu'),
    url(r'^coupons/', 'orderapp.views.coupons', name='coupons'),

    url(r'^admin/', include(admin.site.urls)),


)