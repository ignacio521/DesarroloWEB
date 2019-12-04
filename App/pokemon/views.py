from django.shortcuts import render
from .models import Equipo
from .forms import EquipoForm
from rest_framework import viewsets
from .serializers import EquipoSerializer
from .models import Post


def Home(request):
    posts = Post.objects.filter(estado = True)
    return render(request,'pokemon/index.html',{'posts':posts})

def Anime(request):
    return render(request,'pokemon/index Anime.html')

def Competitivo(request):
    return render(request,'pokemon/index Competitivo.html')

def Manga(request):
    return render(request,'pokemon/index Manga.html')

def Videojuegos(request):
    return render(request,'pokemon/index Videojuegos.html')

def Registro(request):
    return render(request,'pokemon/bruh.html')

def Det_Equipo(request):
    equipo = Equipo.objects.all()
    data = {
       'equipo':equipo
    }
    return render(request,'pokemon/Equipo.html',{'Equipo':equipo})  

def Nuevos_Equipo(request):
    data = {
    'form':EquipoForm()

    }

    if request.method == 'POST':
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
           formulario.save()
           data ['mensaje'] = 'Guardado Correctamente'

    return render(request,'pokemon/Nuevo_Equipo.html', data)

def Modificar_eq(request, id_eq):
    equipo = Equipo.objects.get(id_eq=id_eq)
    data = {
       'form':EquipoForm(instance=equipo)
    }
    if request.method== 'POST':
        formulario = EquipoForm(data=request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    return render(request,'pokemon/Modificar_Equipo.html',data )

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'pokemon/post.html',{'detalle_post':post})
