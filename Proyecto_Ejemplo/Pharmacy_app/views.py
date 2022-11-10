from django.shortcuts import render
from django.template import context
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html',{"username":"usuario"})

def about(request):
    return render(request,'about.html') 

def prueba(request):
    return render(request,'prueba.html')     

def formulario(request):
    return render(request,'formulario.html', {"producto1":"Panadol",
    "producto2":"Acetaminofen"})         