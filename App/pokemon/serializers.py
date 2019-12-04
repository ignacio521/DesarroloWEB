from rest_framework import serializers
from .models import Equipo


class EquipoSerializer(serializers.ModelSerializer):
     
     class Meta:
      model = Equipo
      fields = ['id_eq','nombre_equipo','pokemon_1','pokemon_2','pokemon_3','pokemon_4','pokemon_5','pokemon_6']
      	



