from django import forms
from movies.models import Movies
class MoviesForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    type = forms.CharField(max_length=100, label='Genero')
    duration = forms.FloatField( label='Duracion')
    picture = forms.ImageField(label='Imagen')
    premiered = forms.BooleanField(label='Estrenada', required=False)
    class Meta:
        model = Movies
        fields = ['name','type','duration','picture','premiered']

class StudioForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    creation = forms.DateField(label='Fecha de creacion')

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    films = forms.FloatField(label='Peliculas')

class WindowsForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    tittle =forms.CharField(max_length=100,label='Titulo')
    picture = forms.ImageField(label='Imagen')
    text =forms.CharField(max_length=10000,label='Contenido')
    

