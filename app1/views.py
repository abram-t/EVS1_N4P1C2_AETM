from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1rama1(request):
    html= """
    <h1 style='color:blue'>
    Bienvenido a la rama numero1 de la app1   
    </h1>"""
    return HttpResponse(html)

def vista2rama1(request):
    html= """
    <h1 style='color:blue'>
    Bienvenido a la vista1 de la rama1   
    </h1>"""
    return HttpResponse(html)
