from django import forms

class VotanteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()

class MesaForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    
class ListaForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    numero = forms.CharField(max_length=50)
    
class FiscalForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    partido = forms.CharField(max_length=50)