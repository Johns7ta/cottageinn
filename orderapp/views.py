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
from orderapp.models import Person, Member, Item, ItemCategory, ItemList, Order, OrderItem
from orderapp.forms import UserCreateForm
import simplejson
from django.contrib.auth.models import User


def vibebase(request,template_name="vibebase.html"):
    context = {}
    context['MyCategories'] = ItemCategory.objects.all()

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
def ordersuccess(request,template_name="ordersuccess.html"):
    context = {}
    context[''] = ""

    return render(template_name, context, context_instance=RequestContext(request))

def custlogin(request, template_name="custlogin.html"):
    context = {}
    context.update(csrf(request))
    next = None

    try:
        next = request.GET['next']

    except:
        next = "/categories/"


    auth_frm = AuthenticationForm(data=request.POST or None)
    context['form'] = auth_frm

    if auth_frm.is_valid():
        try:
            user = authenticate(username=auth_frm.cleaned_data['username'], password=auth_frm.cleaned_data['password'])
            login(request, user)
        except Exception:
            pass

            #return the same form and say login failed

        return HttpResponseRedirect('/categories/')

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
def custlogout(request, template_name="custlogin.html"):
    context = {}
    try:
        context['do_not_show_menu'] = True
        logout(request)
        return HttpResponseRedirect("/custlogin/")
    except:
        pass

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
def categories(request, template_name="categories.html"):
    context = {}
    context['MyCategories'] = ItemCategory.objects.all()


    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
def items(request, template_name="items.html"):
    context = {}

    try:
        context['MyItems'] = Item.objects.filter(itemcat__id = request.GET['catid'])
    except Exception:
        pass
        #print "Error: %s" % e

    return render(template_name, context, context_instance=RequestContext(request))

def custcreateacct(request, template_name="custcreateacct.html"):

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
        return render(request, "custcreateacct.html", {
            'form': form,
        })

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
@csrf_exempt
def shopcart(request, template_name="shopcart.html"):
    context = {}

    return render(template_name, context, context_instance=RequestContext(request))

@login_required(login_url='/custlogin/')
@csrf_exempt
def buydata(request):

    def goodbyeNull(list):
        goodList = []
        for x in list:
            if x:
                goodList.append(x)
        return goodList


    context = {}

    try:
        hole = request.GET["holenum"]
        items = goodbyeNull(simplejson.loads(request.GET.get("items",None)))
        course = request.GET["courseid"]
        amount = request.GET["sumprice"]
        coursehole = ('%s %s' % (course, hole))

    except KeyError, e:
        return HttpResponse("Key error. %s" % e)
    except Exception, e:
        return HttpResponse("2nd exception %s" % e)

    if not items:
        return HttpResponse("Failed")

    try:
        myOrder = Order()
        myOrder.course = course
        myOrder.holenum = hole
        myOrder.amount = amount
        myOrder.buyer = request.user
        myOrder.save()
    except Exception, e:
        return HttpResponse("Failed to create order")

    for item in items:
        myOrderItem = OrderItem()
        myOrderItem.itemid = Item.objects.get(pk=item['id'])
        myOrderItem.orderid = myOrder
        myOrderItem.qty = int(item['qty'])
        myOrderItem.save()

    return HttpResponse("Order Successful")


