from django.shortcuts import render
from Blog.models import Post, Categoria

# Create your views here.


# Vista BLOG
def blog(request):

    posts = Post.objects.all
    return render(request, "Blog/blog.html", {"posts":posts})



# Vista CATEGORIA
def categoria(request, categoria_id):
    #Traer las categorias disponibles en la BD
    categoria = Categoria.objects.get(id=categoria_id)

    #Filtrar los posts para esas categorias filtradas
    posts = Post.objects.filter(categorias=categoria)

    return render(request, "Blog/categoria.html", {"categoria":categoria, "posts":posts})