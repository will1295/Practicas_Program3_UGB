from django.shortcuts import render, redirect
from django.template import context
from django.http import HttpResponse
from .models import Clientes
from django.contrib.auth.forms import UserCreationForm

# Create your views here.



def index(request):
    return render(request,'index.html',{"username":"Carlitos",
    "username2":"Maria"})


def about(request):
    return render(request,'about.html') 


def registro(request):
    form = UserCreationForm()

 #   if request.method=="post":
  #      form = UserCreationForm(request.post)
   #     if form.is_valid():
   #         form.save()
    context = {"form":form}
    

    return render(request,'register.html', context)     

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

     