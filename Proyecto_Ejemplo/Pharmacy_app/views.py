from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import Clientes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


@login_required(login_url='/')
def index(request):
    return render(request,'index.html')


@login_required(login_url='/')
def about(request):
    return render(request,'about.html') 


class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email','first_name','last_name']

def registro(request):
    form = Registro()
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado con exito')
    return render(request,'register.html', {"form":form})     

def vistalogin(request):
    if request.method == 'POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
        login(request, user)
        return redirect('principal')

    return render(request,'login.html')     

def cerrarsesion(request):
    logout(request)
    return redirect('/')


def prueba(request):
    return render(request,'prueba.html')     

def formulario(request):
    return render(request,'formulario.html')

def adminclientes(request):
    listacli = Clientes.objects.all()
    return render(request,'clientescrud.html', {"cliente":listacli})

def addclientes(request):
    nombre=request.POST['inputnombre']
    apellido=request.POST['inputapellido']
    edad=request.POST['inputedad']
    direccion=request.POST['inputdir']

    clientes= Clientes.objects.create(
        nombre=nombre, apellido=apellido, edad=edad, direccion=direccion
    )
    return redirect('/clientes')     


def editcliente(request,id):
    clientes=Clientes.objects.get(id=id)
    return render(request,'editcliente.html', {"clientes":clientes})

def guardarcliente(request,id): 
     nombre=request.POST['inputnombre']
     apellido=request.POST['inputapellido']
     edad=request.POST['inputedad']
     direccion=request.POST['inputdir']

     id=Clientes.objects.get(id=id)
     id.nombre=nombre
     id.apellido=apellido
     id.edad=edad
     id.direccion=direccion
     id.save()
     return redirect('/clientes')     

def delcliente(request,id):
    clientes=Clientes.objects.get(id=id)
    clientes.delete()      
    return redirect('/clientes')  

     