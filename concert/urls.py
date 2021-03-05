from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from .views import index,ind,creer_payer_view,creer_ticket_view,creer_artiste_view,creer_evenement_view,creer_organisateur_view
app_name='concert'
urlpatterns=[
    path("", index),
    path("index/", ind,name='index'),
    path("ticket/", creer_ticket_view, name='ticket'),
    path("type_ticket/", creer_payer_view, name='type_ticket'),
    path("artiste/", creer_artiste_view, name='artiste'),
    path("organisateur/", creer_organisateur_view, name='organisateur'),
    path("evenemnet/", creer_ticket_view, name='evenement'),
]