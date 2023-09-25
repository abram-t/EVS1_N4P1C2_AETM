from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def vista1rama2(request):
    html= """
    <h1 style='color:blue'>
    Bienvenido a la vista1 de la rama2 
    </h1>"""
    return HttpResponse(html)

def vista2rama2(request):
    html= """
    <h1 style='color:blue'>
    Bienvenido a la vista2 de la rama2   
    </h1>"""
    return HttpResponse(html)
