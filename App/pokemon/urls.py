from django.urls import path, include
from .views import Home
from .views import Anime
from .views import Competitivo
from .views import Manga
from .views import Videojuegos
from .views import Registro
from .views import Det_Equipo
from .views import Nuevos_Equipo
from .views import Modificar_eq	
from .views import EquipoViewSet
from rest_framework import routers
from .views import detallePost

router = routers.DefaultRouter()
router.register('equipo',EquipoViewSet)

urlpatterns = [
path('',Home, name = 'index'),
path('Anime',Anime, name = 'index Anime'),
path('Competitivo',Competitivo, name = 'index Competitivo'),
path('Manga',Manga, name = 'index Manga'),
path('Videojuegos',Videojuegos, name = 'index Videojuegos'),
path('Registro',Registro, name ='Bruh'),
path('Equipo',Det_Equipo, name='Equipos'),
path('Nuevo_Equipo',Nuevos_Equipo, name='Nuevos_Equipos'),
path('Modificar_Equipo/<id_eq>',Modificar_eq, name='Modificar Equipo'),
path('api/', include(router.urls)),
path('<slug:slug>/',detallePost, name = 'detalle_post')

]
