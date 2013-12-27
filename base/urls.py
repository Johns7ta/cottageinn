from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^orderbase/', 'orderapp.views.orderbase', name='orderbase'),

    url(r'^admin/', include(admin.site.urls)),


)