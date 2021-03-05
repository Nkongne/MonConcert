
from __future__ import unicode_literals
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from .models import Invite
from .form import ticketForm,payerForm,organisationForm,artisteForm,evenementForm
import datetime
# Create your views here.
def index(request):

    return  HttpResponse(render(request, 'concert/index.html'))
def ind(request):
    invites=Invite.objects.all()
    t=loader.get_template('concert/index.html')
    c={'invites':Invite}
    #context_dict=c.flatten()
    return  HttpResponse(render(request, 'concert/index.html', c))
def creer_ticket_view(request):
    form=ticketForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ticketForm
    context={
        'form':form
    }
    return render(request,'concert/ticket.html',context)
def creer_payer_view(request):
    form=payerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=payerForm
    context={
        'form':form
    }
    return render(request,'concert/payer.html',context)
def creer_evenement_view(request):
    form=evenementForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=evenementForm
    context={
        'form':form
    }
    return render(request,'concert/evenement.html',context)
def creer_organisateur_view(request):
    form=organisationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=organisationForm
    context={
        'form':form
    }
    return render(request,'concert/organisateur.html',context)
def creer_artiste_view(request):
    form=artisteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=artisteForm
    context={
        'form':form
    }
    return render(request,'concert/artiste.html',context)