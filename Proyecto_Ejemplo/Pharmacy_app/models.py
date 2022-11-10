from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    apellido=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    direccion=models.TextField()

    def __str__(self):
        return str(self.nombre)

class Fabricante(models.Model):
    nombre=models.CharField(max_length=200)
    telefono=models.CharField(max_length=8)
    contacto=models.CharField(max_length=200)


class Productos(models.Model):
    nombre=models.CharField(max_length=200, null=True)
    descripcion=models.TextField()
    stock=models.IntegerField()
    fabricante=models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    fecha_expedicion=models.DateField()
    fecha_expiracion=models.DateField()

    def __str__(self):
        return str(self.nombre)


class Empleados(models.Model):
    codigo=models.CharField(max_length=8, null=True)
    nombre=models.CharField(max_length=200, null=True)
    apellido=models.CharField(max_length=200, null=True)
    edad=models.IntegerField(default='0')
    direccion=models.TextField()

    def __str__(self):
        return str(self.nombre)


class Pedido(models.Model):
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fechahora=models.DateTimeField()

    