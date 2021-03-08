
from __future__ import unicode_literals
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa
#from twilio.rest import Client
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from .models import Invite,Evenement,Artiste,Organisation,Ticket
from django.core.mail import send_mail
from MonConcert.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMessage

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
    sub = ticketForm()
    if request.method == 'POST':
        sub = ticketForm(request.POST)
        subject = 'ton pass est valide'
        message = 'merci de nous faire confiance'
        recepient = str(sub['email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'concert/envoi_success.html', {'recepient': recepient})
        return render(request, 'concert/index.html', {'form': sub})

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

    msg = EmailMessage('invitation', 'vous etes invite a prendre part au showbiz', 'nkongnedev@gmail.com', ['to@email.com'])
    msg.content_subtype = "html"
    msg.attach_file('pdfs/Instructions.pdf')
    msg.send()

    return render(request,'concert/artiste.html',context)
def send_sms(request):
    message = 'Add Your Me'
    frome= '+12019043654 '
    to = '+237697313751'
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    response = client.messages.create(body=message, to=to, frome=frome)
    return HttpResponse("SMS Sent")
def envoyer(request):
    sub =ticketForm()
    if request.method == 'POST':
        sub = ticketForm(request.POST)
        subject = 'ton pass est valide'
        message = 'merci de nous faire confiance'
        recepient = str(sub['email'].value())

        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        return render(request, 'concert/envoi_success.html', {'recepient': recepient})
    return render(request, 'concert/index.html', {'form':sub})
def pdf_invites(request):
    all_invites = Invite.objects.all().order_by("nom")
    context = {
       'all_invites':all_invites
    }

    template = get_template('concert/ticket/invite_pdf.html')
    html  = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')
def pdf_artistes(request):
    all_artistes = Artiste.objects.all().order_by("nom")
    context = {
       'all_artistes':all_artistes
    }

    template = get_template('concert/ticket/artiste_pdf.html')
    html  = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')
def imprimer(request):
    all_events = Evenement.objects.all()
    all_tickets= Ticket.objects.all()
    all_invites= Invite.objects.all()
    context = {
         'all_events':all_events,
        'all_tickets': all_tickets,
        'all_invites': all_invites

    }

    template = get_template('concert/ticket/billet_pdf.html')
    html  = template.render(context)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')