from django.db import models

# Create your models here.

class Ticket(models.Model):
    payer=[('Pass','Pass'),
           ('Reservation','Reservation')]
    montant=models.BigIntegerField(default=5000)
    type=models.CharField(max_length=20,choices=payer)
    def __str__(self):
        return  self.type
class Meta:
    proxy=True

class PassManager(models.Model):
    def get_queryset(self):
        return super(PassManager, self).get_queryset().filter(payer='Pass')
class Pass(Ticket):
    object=PassManager()

class Meta:
    proxy=True

class ReservationManager(models.Model):
    def get_queryset(self):
        return super(ReservationManager, self).get_queryset().filter(payer='Reservation')
class Reservation(Ticket):
    object=ReservationManager()

class Invite (models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    tel=models.CharField(max_length=30)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Evenement(models.Model):
    description=models.CharField(max_length=50)
    heureEvent=models.DateTimeField('programmer le')
    lieuEvent=models.CharField('Lieu evenement:',max_length=30)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)


class Organisation (models.Model):
    nom=models.CharField(max_length=50)
    evenement=models.ManyToManyField(Evenement)
    tel=models.CharField(max_length=30)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return self.nom

class Artiste (models.Model):
    nom=models.CharField(max_length=50)
    evenement=models.ManyToManyField(Evenement)
    tel=models.CharField(max_length=30)
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return self.nom