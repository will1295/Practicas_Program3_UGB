from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Fabricante)
admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Pedido)