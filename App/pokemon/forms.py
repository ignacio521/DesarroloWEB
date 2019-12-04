from django import forms
from django.forms import ModelForm
from .models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['id_eq','nombre_equipo','pokemon_1','pokemon_2','pokemon_3','pokemon_4','pokemon_5','pokemon_6']
        
