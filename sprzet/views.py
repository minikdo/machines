from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Kompy, Serwis, Sprzet, SprzetTyp
from django.urls import reverse_lazy, reverse
import time


class IndexView(generic.ListView):
    template_name = 'sprzet/index.html'
    context_object_name = 'kompy'
    
    def get_queryset(self):
        return Kompy.objects.order_by('pk')
    

class DetailView(generic.DetailView):
    model = Kompy
    template_name = 'sprzet/detail.html'

    def get_queryset(self):
        qs = super(DetailView, self).get_queryset()
        return qs.select_related()     


class SerwisIndexView(generic.ListView):
    template_name = 'sprzet/serwis_index.html'
    context_object_name = 'serwisy'
    model = Serwis
    

class SerwisCreate(CreateView):
    """
    Dodawanie czynności serwisowej
    """
    model = Serwis
    fields = ['komp', 'data', 'czynnosc']

    def get_initial(self, **kwargs):
        return {'komp': self.request.GET.get("komp_id", None), 'data': time.strftime('%Y-%m-%d')}


class SerwisUpdate(UpdateView):
    """
    Uaktualnienie czynności serwisowej
    """
    model = Serwis
    fields = ['komp', 'data', 'czynnosc']
    
    
class SerwisDelete(DeleteView):
    """
    Usuwanie czynności serwisowej
    """
    model = Serwis

    def get_success_url(self):
        komp = self.object.komp
        return reverse_lazy('detail', kwargs={'pk': komp.pk})

