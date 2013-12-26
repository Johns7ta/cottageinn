# Create your views here.
import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response as render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from empapp.models import Employee
from orderapp.models import

def empbase(request,template_name="empbase.html"):
    context = {}
    context['FutureTemplateVariable'] = "The Value of the Future Template Variable"

    return render(template_name, context, context_instance=RequestContext(request))

def emplogin(request,template_name="emplogin.html"):
    context = {}
    context.update(csrf(request))
    next = None

    try:
        next = request.GET['next']

    except:
        next = "/requestedorders/"


    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:
            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)
        except Exception:
            pass

            #return the same form and say login failed

        return HttpResponseRedirect('/requestedorders/')

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/emplogin/')
def requestedorders(request,template_name="requestedorders.html"):
    context = {}
    context['myOrders'] = OrderItem.objects.filter(orderid__is_closed=None)


    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/emplogin/')
def custlookup(request, template_name="custlookup.html"):
    context = {}
    context['Customers'] = User.objects.all()

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/emplogin/')
def closeOrder(request):
    try:
        orderid = request.GET.get('orderid', None)
        myOrder = Order.objects.get(pk=orderid)
        myOrder.is_closed = datetime.datetime.now()
        myOrder.save()
        return HttpResponse("ok")
    except Exception, e:
        return HttpResponse("Error. %s" % e)