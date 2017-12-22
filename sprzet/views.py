from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Kompy, Serwis, Sprzet, SprzetTyp, KompySprzet
from django.urls import reverse_lazy, reverse
import time


class IndexView(generic.ListView):
    """
    Lista hostów
    """
    template_name = 'sprzet/index.html'
    context_object_name = 'kompy'
    
    def get_queryset(self):
        return Kompy.objects.order_by('pk')
    

class DetailView(generic.DetailView):
    """
    Szczegóły hosta
    """
    model = Kompy
    template_name = 'sprzet/detail.html'


class SerwisIndexView(generic.ListView):
    """
    Lista czynności serwisowych
    """
    template_name = 'sprzet/serwis_index.html'
    context_object_name = 'serwisy'
    model = Serwis
    ordering = '-data'
    paginate_by = 10
    

class SerwisCreate(CreateView):
    """
    Dodawanie czynności serwisowej
    """
    model = Serwis
    fields = ['komp', 'data', 'czynnosc', 'sprzet']

    def get_initial(self, **kwargs):
        return {'komp': self.request.GET.get("komp_id", None),
                'data': time.strftime('%Y-%m-%d')}


class SerwisUpdate(UpdateView):
    """
    Uaktualnienie czynności serwisowej
    """
    model = Serwis
    fields = ['komp', 'data', 'czynnosc', 'sprzet']
    
    
class SerwisDelete(DeleteView):
    """
    Usuwanie czynności serwisowej
    """
    model = Serwis

    def get_success_url(self):
        komp = self.object.komp
        return reverse_lazy('detail', kwargs={'pk': komp.pk})


class SprzetIndexView(generic.ListView):
    """
    Lista sprzętu
    """
    template_name = 'sprzet/sprzet_index.html'
    context_object_name = 'sprzet'
    model = Sprzet
    paginate_by = 10                                                        
    ordering = '-data'


class SprzetDetailView(generic.DetailView):
    """
    Widok szczegółowy sprzętu
    """
    model = Sprzet
    template_name = 'sprzet/sprzet_detail.html'


class SprzetCreate(CreateView):
    """
    Dodawanie sprzętu
    """
    model = Sprzet
    fields = ['data', 'typ', 'nazwa', 'cena', 'firma', 'numer']

    def get_initial(self, **kwargs):
        return {'data': time.strftime('%Y-%m-%d')}

    
class SprzetUpdate(UpdateView):
    """
    Uaktualnienie sprzętu
    """
    model = Sprzet
    fields = ['data', 'typ', 'nazwa', 'cena', 'firma', 'numer']
    
    
class SprzetDelete(DeleteView):
    """
    Usuwanie sprzętu
    """
    model = Sprzet
    success_url = reverse_lazy('sprzet-index')
    

class KompySprzetCreate(CreateView):
    """
    Łączenie hostów ze sprzętem
    """
    model = KompySprzet
    fields = ['komp', 'sprzet']
    
    def get_initial(self, **kwargs):
        return {'komp': self.request.GET.get("komp_id", None)}

