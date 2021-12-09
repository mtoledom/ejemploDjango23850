from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Primer vista
def inicio(request):
    #return HttpResponse("Esto es una prueba de inicio")
    return render(request,'Appcoder/inicio.html')

def jugadores(request):
    #return HttpResponse("Esto es una prueba de inicio")
    return render(request,'Appcoder/jugadores.html')
