from django.conf.urls import patterns, include, url
from django.contrib.auth import authenticate, login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^custlogin/', 'orderapp.views.custlogin', name='custlogin'),

    url(r'^admin/', include(admin.site.urls)),


)