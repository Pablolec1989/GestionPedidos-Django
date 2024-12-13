from django.shortcuts import render
from . models import Producto

# Create your views here.

def tienda(request):
    
    #Traer todos los productos
    productos = Producto.objects.all 
    
    return render(request, "Tienda/tienda.html", {"productos":productos})
