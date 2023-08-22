from django.urls import path

from .views import inicio,votanteFormulario,fiscalFormulario,listaFormulario,mesaFormulario,votantes,fiscales,listas,mesas

urlpatterns = [
    path('', inicio),
    path('votanteFormulario',votanteFormulario,name="votanteFormulario"),
    path('fiscalFormulario',fiscalFormulario,name="fiscalFormulario"),
    path('listaFormulario',listaFormulario,name="listaFormulario"),
    path('mesaFormulario',mesaFormulario,name="mesaFormulario"),
    path('votantes',votantes,name="votantes"),
    path('fiscales',fiscales,name="fiscales"),
    path('listas',listas,name="listas"),
    path('mesas',mesas,name="mesas"),
]
