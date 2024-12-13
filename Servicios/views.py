from django.shortcuts import render

from Servicios.models import Servicio

# Create your views here.


def servicios(request):

    servicios=Servicio.objects.all #Importar todos los servicios construidos en admin

    return render(request, "Servicios/servicios.html", {"servicios":servicios})