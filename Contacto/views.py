from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

# Clase Contacto
def contacto(request):

    formulario_contacto = FormularioContacto()

    # Rescatar datos de formulario la info que el usuario 
    if(request.method == "POST"):
        formulario_contacto = FormularioContacto(data = request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # Datos para email:
            email = EmailMessage("Mensaje desde proyecto de DJANGO",
                                  "El usuario {} desde la dirección {} escribe lo siguiente: \n\n {}"
                                  .format(nombre, email,contenido), 
                                  "",["pabloleccese6@gmail.com"],reply_to=[email])
            
            try:
                email.send()

                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")
    
    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})