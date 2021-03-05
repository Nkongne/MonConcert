from django import forms
from .models import Invite,Ticket,Evenement,Organisation,Artiste
class ticketForm(forms.ModelForm):
    class Meta:
        model=Invite
        fields=[
            'nom',
            'prenom',
            'tel',
            'email',
            'ticket',

        ]
class evenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = [
            'description',
            'heureEvent',
            'lieuEvent',
            'ticket',
            ]


class organisationForm(forms.ModelForm):
        class Meta:
            model = Organisation
            fields = [
                'nom',

                'tel',
                'email',
                'evenement',

            ]
class payerForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=[
            'montant',
            'type',


        ]
class artisteForm(forms.ModelForm):
    class Meta:
        model=Artiste
        fields=[
            'nom',

            'tel',
            'email',
            'evenement',

        ]