from django.shortcuts import redirect, render

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    
    
    def post(self, request):
        form = UserCreationForm(request.POST) #Del metodo post del formulario vienen todos los datos
        
        if(form.is_valid()):
            usuario = form.save() # Guardo la informacion (user/pass)
            login(request, usuario)
            return redirect("Home")
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, "registro/registro.html", {"form":form})
        

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")


def loguear(request):
    
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username") #Rescatar info del formulario
            pass_usuario = form.cleaned_data.get("password")
            
            # Verificacion de datos con 'Authenticate'
            usuario = authenticate(username = nombre_usuario, password = pass_usuario)
            
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no válido")
        
        else:
            messages.error(request, "Información incorrecta")
            
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})
    
    