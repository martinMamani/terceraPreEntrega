from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Fiscal,Votante,Mesa,Lista

from .forms import VotanteForm,MesaForm,ListaForm,FiscalForm


def inicio(request):
    return render(request,'elecciones/inicio.html')


def votantes(request):
    votantes = Votante.objects.all()
    return render(request,"elecciones/votantes.html",{"votantes":votantes})

def fiscales(request):
    fiscales = Fiscal.objects.all()
    return render(request,"elecciones/fiscales.html",{"fiscales":fiscales})

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request,"elecciones/mesas.html",{"mesas":mesas})

def listas(request):
    listas = Lista.objects.all()
    return render(request,"elecciones/listas.html",{"listas":listas})

def votanteFormulario(request):
    formulario_votante = VotanteForm()
    if request.method == "POST":
        form = VotanteForm(request.POST)
        if form.is_valid():
            dataFiltrada = form.cleaned_data
            nombre = dataFiltrada["nombre"]
            apellido = dataFiltrada["apellido"]
            dni = dataFiltrada["dni"]
            votante = Votante(nombre=nombre,apellido=apellido,dni=dni)
            votante.save()
            return render(request,"elecciones/votanteFormulario.html",{"mensaje":"Votante creado","formulario":formulario_votante})
        return render(request,"elecciones/votanteFormulario.html",{"mensaje":"Datos invalidos"})
    else:
        return render(request,"elecciones/votanteFormulario.html",{"formulario":formulario_votante})
    

def fiscalFormulario(request):
    formulario_fiscal = FiscalForm()
    if request.method == "POST":
        form = FiscalForm(request.POST)
        if form.is_valid():
            dataFiltrada = form.cleaned_data
            nombre = dataFiltrada["nombre"]
            apellido = dataFiltrada["apellido"]
            dni = dataFiltrada["dni"]
            partido = dataFiltrada["partido"]
            fiscal = Fiscal(nombre=nombre,apellido=apellido,dni=dni,partido=partido)
            fiscal.save()
            return render(request,"elecciones/fiscalFormulario.html",{"mensaje":"Fiscal creado","formulario":formulario_fiscal})
        return render(request,"elecciones/fiscalFormulario.html",{"mensaje":"Datos invalidos"})
    else:
        return render(request,"elecciones/fiscalFormulario.html",{"formulario":formulario_fiscal})
    

def listaFormulario(request):
    formulario_lista = ListaForm()
    if request.method == "POST":
        form = ListaForm(request.POST)
        if form.is_valid():
            dataFiltrada = form.cleaned_data
            nombre = dataFiltrada["nombre"]
            numero = dataFiltrada["numero"]
            lista = Lista(nombre=nombre,numero=numero)
            lista.save()
            return render(request,"elecciones/listaFormulario.html",{"mensaje":"Lista creada","formulario":formulario_lista})
        return render(request,"elecciones/listaFormulario.html",{"mensaje":"Datos invalidos"})
    else:
        return render(request,"elecciones/listaFormulario.html",{"formulario":formulario_lista})


def mesaFormulario(request):
    formulario_mesa = MesaForm()
    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            dataFiltrada = form.cleaned_data
            nombre = dataFiltrada["nombre"]
            mesa = Mesa(nombre=nombre)
            mesa.save()
            return render(request,"elecciones/mesaFormulario.html",{"mensaje":"Mesa creada","formulario":formulario_mesa})
        return render(request,"elecciones/mesaFormulario.html",{"mensaje":"Datos invalidos"})
    else:
        return render(request,"elecciones/mesaFormulario.html",{"formulario":formulario_mesa})