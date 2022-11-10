from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    telefono=models.CharField(max_length=8)
    direccion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre+' '+self.apellido


class TipoC(models.Model):
    tipo=models.CharField(max_length=200)
    def __str__(self):
        return self.tipo

                  

class Cuenta(models.Model):
    ncuenta=models.CharField(max_length=10)
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    monto=models.DecimalField(decimal_places=2, max_digits=10)
    tipo=models.ForeignKey(TipoC, on_delete=models.CASCADE)
    def __str__(self):
        return 'Nº Cuenta: '+str(self.ncuenta)


class Transaccion(models.Model):
    ncuenta=models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha=models.DateTimeField()
    monto=models.DecimalField(decimal_places=2, max_digits=10) 
    cuentadestino=models.CharField(max_length=10)   
    def __str__(self):
        return 'Fecha: '+str(self.fecha)

