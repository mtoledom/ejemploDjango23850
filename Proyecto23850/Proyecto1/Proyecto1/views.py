from django import http
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

#paso 1
from django.template import loader

def saludo(request):
    return HttpResponse("Hola soy Miguel, estoy programando")

def segundaVista(request):
    return HttpResponse("<h1>-------YA SOMOS PROGRAMADORES WEB--------</h1>")

def dia(request):
    variable =datetime.now()
    return HttpResponse(f"<h5>Hoy es una gran día {variable}</h5>")

def apellido(request, ape):
    fecha =datetime.now()
    return HttpResponse(f"El profe de Coder {ape} es muy bueno..<br><br>.. Por lo menos hoy: {fecha}")


def probandoTemplate(request):
    mejorEstudiante="Ilan Fitzler"

    nota= 8.9
    
    fecha=datetime.now()

    estudiantes =["Juanse", "Nadia", "Cristo", "Laura"]

    dicc={"nombre": mejorEstudiante, "nota":nota, "fecha":fecha, "estudiantes":estudiantes}

    plantilla =loader.get_template("template1.html")


    #miHTML = open("C:/Users/mtoledo/Desktop/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

   #plantilla =Template(miHTML.read())

    #miHTML.close()

   # miContexto = Context(dicc)

    documento = plantilla.render(dicc)

    return HttpResponse(documento)