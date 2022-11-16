from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clientes

# Create your views here.

def index(request):
    return render(request,'index.html',{"username":"Carlitos",
    "username2":"Maria"})

def acercade(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')

def registro(request):
    return render(request,'registro.html')

def clientes(request):
    clientes = Clientes.objects.all()
    return render(request,'clientescrud.html',{"clientes":clientes})

def regclientes(request):
    codigo=request.POST['inputcodigo']
    nombre=request.POST['inputnombre']
    apellido=request.POST['inputapellido']
    telefono=request.POST['inputtelefono']
    direccion=request.POST['inputdireccion']
    clientes = Clientes.objects.create(
        codigo=codigo, nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion)
    return redirect('/')







