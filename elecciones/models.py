from django.db import models

# Create your models here.


class Votante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(8)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} con dni {self.dni}"


class Mesa(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Lista(models.Model):
    nombre= models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} - {self.numero}"
    
class Fiscal(models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(8)
    partido = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido} con dni {self.dni} y partido {self.partido}"