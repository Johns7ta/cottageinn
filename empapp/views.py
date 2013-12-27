# Create your views here.
import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response as render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from empapp.models import *
from orderapp.models import *

def empbase(request,template_name="empbase.html"):
    context = {}
    context['FutureTemplateVariable'] = "The Value of the Future Template Variable"

    return render(template_name, context, context_instance=RequestContext(request))