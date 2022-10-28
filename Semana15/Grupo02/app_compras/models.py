from tkinter import CASCADE
from django.db import models

# Create your models here.

#Declaracion de tablas para el model
class tblClientes(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    dui=models.CharField(max_length=9)
    direccion=models.TextField()
    edad=models.CharField(max_length=3)
    genero=models.CharField(max_length=20)
    telefono=models.CharField(max_length=8)


class tblProveedores(models.Model):
    nombre=models.CharField(max_length=200)
    fechacarga=models.DateField()
    telefono=models.CharField(max_length=200)

class tblEmpleados(models.Model):
    codigo=models.CharField(max_length=6)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    horario=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    

class tblSucursales(models.Model):
    nombre=models.CharField(max_length=200)
    direccion=models.TextField()
    telefono=models.CharField(max_length=200)


class tblProductos(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    existencia=models.CharField(max_length=200)
    proveedor=models.ForeignKey(tblProveedores, on_delete=models.CASCADE)
    sucursal=models.ForeignKey(tblSucursales, on_delete=models.CASCADE)








