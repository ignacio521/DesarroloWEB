from django.db import models
from ckeditor.fields import RichTextField

class Equipo(models.Model):
    pass
    id_eq = models.AutoField(primary_key = True)
    nombre_equipo= models.CharField('nombre_equipo', max_length = 200, blank = False, null = False)
    pokemon_1 = models.CharField('pokemon_1', max_length = 200, blank = False, null = False)
    pokemon_2 = models.CharField('pokemon_2', max_length = 200, blank = False, null = False)
    pokemon_3 = models.CharField('pokemon_3', max_length = 200, blank = False, null = False)
    pokemon_4 = models.CharField('pokemon_4', max_length = 200, blank = False, null = False)
    pokemon_5 = models.CharField('pokemon_5', max_length = 200, blank = False, null = False)
    pokemon_6 = models.CharField('pokemon_6', max_length = 200, blank = False, null = False)


class Meta:
         verbose_name = 'Equipo'
def __str__(self):
    return self.nombre_equipo

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False, default = 'Codigo')
    contenido = RichTextField('Contenido')
    imagen = models.URLField(max_length = 255, blank = False, null = False)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural ="Posts"

    def __str__(self):
        return self.titulo


