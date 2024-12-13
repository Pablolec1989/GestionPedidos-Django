from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Carro.carro import Carro
from Pedidos.models import Linea_pedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail



# Create your views here.

@login_required(login_url = "/autenticacion/loguear")
def procesar_pedido(request):
    
    pedido = Pedido.objects.create(user = request.user) #Reconoce el usuario que hace el pedido.
    
    # Recorremos los items del carro para almacenarlos en el pedido
    
    carro = Carro(request)
    lineas_pedido = list()
    
    # Recorro el carro, rescato informacion para meterlo en una lista.('Linea_Pedido')
    for key,value in carro.carro.items():
        lineas_pedido.append(Linea_pedido(
            
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido,
        ))
        
    # Inserto en BD el pedido 'bulk create' hace lotes de insert en BD.
    Linea_pedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email,
    )
    
    messages.success(request, "El pedido se ha creado exitosamente")
    
    return redirect("Tienda")
    
def enviar_mail(**kwargs):
    
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{
        
        "pedido" : kwargs.get("pedido"),
        "lineas_pedido" : kwargs.get("lineas_pedido"),
        "nombreusuario" : kwargs.get("nombreusuario")
        
        })
    
    # 'strip_tags' omite las etiquetas de tipo 'html'
    mensaje_texto = strip_tags(mensaje)
    from_email = "pabloleccese6@gmail.com"
    to = kwargs.get("emailusuario")
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)