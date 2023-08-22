from django.contrib import admin

# Register your models here.

from .models import Fiscal,Votante,Mesa,Lista

admin.site.register(Fiscal)
admin.site.register(Votante)
admin.site.register(Mesa)
admin.site.register(Lista)

