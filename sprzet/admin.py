from django.contrib import admin

from .models import Kompy, Serwis, SprzetTyp, Sprzet

admin.site.register(Kompy)
admin.site.register(Serwis)
admin.site.register(Sprzet)
admin.site.register(SprzetTyp)
