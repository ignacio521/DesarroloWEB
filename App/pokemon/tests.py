from django.test import TestCase
from .models import Equipo 
from .models import Post

class EquipoTestCase(TestCase):
 def setUp(self):
  Equipo.objects.create( nombre_equipo = 'Fantasma', pokemon_1 = 'Haunter', pokemon_2= "Gastly", pokemon_3= "Gengar" , pokemon_4= "Mimikyu" , pokemon_5= "Dusknoir", pokemon_6= "Giratina")
  
 def test_Equipo_Pokemon1(self):
  Equipo1 = Equipo.objects.get(nombre_equipo="Fantasma")
  self.assertEqual(Equipo1.pokemon_1, "Haunter")  

 







    