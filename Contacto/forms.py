from django import forms

# Clase formulario para contacto
class FormularioContacto(forms.Form):

    nombre = forms.CharField(label = "Nombre", required = True, max_length=50)
    email = forms.CharField(label = "Email", required = True, max_length=50)
    contenido = forms.CharField(label = "Contenido", widget = forms.Textarea, max_length=300)

