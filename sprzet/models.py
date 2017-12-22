from django.db import models
from django.urls import reverse


class Kompy(models.Model):
    name = models.CharField(max_length=50)
    FQDN = models.CharField(max_length=50, null=True)
    datetime = models.DateField()
    form = models.CharField(max_length=50, null=True)
    bios = models.CharField(max_length=50, null=True)
    prod = models.CharField(max_length=50, null=True)
    vendor = models.CharField(max_length=50, null=True)
    OS = models.CharField(max_length=50, null=True)
    kernel = models.CharField(max_length=50, null=True)
    CPU = models.CharField(max_length=50, null=True)
    cores = models.CharField(max_length=50, null=True)
    arch = models.CharField(max_length=50, null=True)
    mem = models.CharField(max_length=50, null=True)
    HDD = models.CharField(max_length=50, null=True)
    disk = models.CharField(max_length=50, null=True)
    diskfree = models.CharField(max_length=50, null=True)
    IPs = models.CharField(max_length=50, null=True)
    gateway = models.CharField(max_length=50, null=True)
    gate_iface = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.FQDN


class Serwis(models.Model):
    komp = models.ForeignKey('Kompy', on_delete=models.CASCADE)
    data = models.DateField()
    czynnosc = models.CharField(max_length=300)
    sprzet = models.ForeignKey('Sprzet', blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.komp_id})

    def __str__(self):
        return self.czynnosc


class Sprzet(models.Model):
    komp = models.ForeignKey('Kompy', blank=True, null=True, on_delete=models.CASCADE)
    data = models.DateField()
    typ = models.ForeignKey('SprzetTyp', on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=150, null=True)
    cena = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    firma = models.CharField(max_length=150, blank=True, null=True)
    numer = models.CharField(max_length=150, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('sprzet-index')

    def __str__(self):
        return str(self.data) + ' ' + self.nazwa 


class SprzetTyp(models.Model):
    nazwa = models.CharField(unique=True, max_length=150, null=True)

    def __str__(self):
        return self.nazwa


    
