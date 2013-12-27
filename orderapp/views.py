import datetime
from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response as render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import simplejson


def orderbase(request,template_name="orderbase.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))


