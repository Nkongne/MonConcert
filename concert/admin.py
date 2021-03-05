from django.contrib import admin

# Register your models here.
from .models import Invite, Ticket, Evenement, Artiste, Organisation
app_name = 'concert'


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom']
    search_fields = ['nom', 'prenom']


@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'tel']
    search_fields = ['nom', 'tel']


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'tel']
    search_fields = ['nom', 'tel', 'email']


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ['description', 'heureEvent']
    search_fields = ['description', 'heureEvent']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['type']
    search_fields = ['type']
