from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clientes
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request,'index.html',{"username":"Carlitos",
    "username2":"Maria"})

def acercade(request):
    
    return render(request,'about.html')

def registro(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'registro.html', {"form":form})


def base(request):
    return render(request,'base.html')

def adminclientes(request):
    clientes= Clientes.objects.all()
    return render(request,'adminclientes.html', {"clientes":clientes})

def agregarcliente(request):
    codigo= request.POST['inputcodigo']
    nombre= request.POST['inputnombre']
    apellido= request.POST['inputapellido']
    telefono= request.POST['inputtelefono']
    direccion= request.POST['inputdir']

    clientes= Clientes.objects.create(
        codigo=codigo, nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion
    )  
    return redirect('/adminclientes')

def editclientes(request,id):
    clientes = Clientes.objects.get(id=id)
    return render(request,'editclientes.html', {"clientes":clientes})

def actualizarclientes(request,id):
    codigo= request.POST['inputcodigo']
    nombre= request.POST['inputnombre']
    apellido= request.POST['inputapellido']
    telefono= request.POST['inputtelefono']
    direccion= request.POST['inputdir']
    
    cliente = Clientes.objects.get(id=id)
    cliente.codigo=codigo
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.save()
    return redirect('/adminclientes')
    

def delclientes(request, id):
    clientes = Clientes.objects.get(id=id)
    clientes.delete()
    return redirect('/adminclientes')







