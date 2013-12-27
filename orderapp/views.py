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
from orderapp.forms import UserCreateForm
from django.contrib.auth.models import User
import simplejson


def orderbase(request,template_name="orderbase.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def custlogin(request, template_name="custlogin.html"):
    context = {}
    context.update(csrf(request))
    next = None

    try:
        next = request.GET['next']

    except:
        next = ""


    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:
            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)
        except Exception:
            pass

            #return the same form and say login failed

        return HttpResponseRedirect('')

    return render(template_name, context, context_instance=RequestContext(request))

def createacct(request, template_name="createacct.html"):
    context = {}
    context.update(csrf(request))
    next = None

    try:
        next = request.GET['next']

    except:
        next = "/custlogin/"


    create_form = UserCreateForm(data=request.POST or None)
    context['form'] = create_form

    if request.method == 'POST':
        form = create_form
        if form.is_valid():
            try:
                new_user = form.save()
                return HttpResponseRedirect('/custlogin/')
            except:
                return HttpResponse("Cannot save form.")
        else:
            form = create_form
        return render(request, "createacct.html", {
            'form': form,
        })

    return render(template_name, context, context_instance=RequestContext(request))

def delivery(request,template_name="delivery.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def carryout(request,template_name="carryout.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def delorder(request,template_name="delorder.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def delinfo(request,template_name="delinfo.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def colocation(request,template_name="colocation.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def coorder(request,template_name="coorder.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def menu(request,template_name="menu.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def pizza(request,template_name="pizza.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def coupons(request,template_name="coupons.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))

def shopcart(request,template_name="shopcart.html"):
    context = {}
    context['MyOrders'] = "Future Fun"

    return render(template_name, context, context_instance=RequestContext(request))