from django.db import models

# Create your models here.

class tblProveedor(models.Model):
    nombre= models.CharField(max_length=200)
    direccion= models.TextField()
    nombrecont=models.CharField(max_length=200)
    telefono=models.CharField(max_length=8)

class tblSucursales(models.Model):
    nombre= models.CharField(max_length=200)
    direccion= models.TextField()
    telefono=models.CharField(max_length=8)
    horarioap=models.TimeField()
    horariocier=models.TimeField()

class tblEmpleados(models.Model):
    codigo= models.CharField(max_length=10)
    nombre= models.CharField(max_length=200)
    apellidos= models.CharField(max_length=200)
    cargo= models.CharField(max_length=200)
    sucursal=models.ForeignKey(tblSucursales, on_delete=models.CASCADE)
    turno=models.CharField(max_length=20)    

class tblProductos(models.Model):
    codigo= models.CharField(max_length=10)
    nombre= models.CharField(max_length=200)
    descripcion= models.TextField()
    stock=models.IntegerField()
    sucursal=models.ForeignKey(tblSucursales, on_delete=models.CASCADE)
    proveedor=models.ForeignKey(tblProveedor, on_delete=models.CASCADE)
    fechacad=models.DateField()

class Entradas(models.Model):
    producto=models.ForeignKey(tblProductos, on_delete=models.CASCADE)
    cantidadent=models.IntegerField()
    proveedor=models.ForeignKey(tblProveedor, on_delete=models.CASCADE)
    empleado=models.ForeignKey(tblEmpleados, on_delete=models.CASCADE)
    fechahor=models.DateTimeField()

class Salidas(models.Model):
    producto=models.ForeignKey(tblProductos, on_delete=models.CASCADE)
    cantidadsal=models.IntegerField()
    proveedor=models.ForeignKey(tblProveedor, on_delete=models.CASCADE)
    empleado=models.ForeignKey(tblEmpleados, on_delete=models.CASCADE)
    fechahor=models.DateTimeField()

