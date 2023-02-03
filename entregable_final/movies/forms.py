from django import forms
from movies.models import Movies,Studio,Director,Windows
class MoviesForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    type = forms.CharField(max_length=100, label='Genero')
    duration = forms.FloatField( label='Duracion')
    picture = forms.ImageField(label='Imagen',required=False)
    premiered = forms.BooleanField(label='Estrenada', required=False)
    date = forms.DateField(label='Fecha de estreno',required=False)
    class Meta:
        model = Movies
        fields = ['name','type','duration','picture','premiered']

class StudioForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    creation = forms.DateField(label='Fecha de creacion')
    place = forms.CharField(max_length=100,label='Ubicacion')
    image = forms.ImageField(label='Imagen',required=False)
    class Meta:
        model = Studio
        fields = ['name','creation','place','image']

class DirectorForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    films = forms.FloatField(label='Peliculas')
    birth= forms.DateField(label='Fecha de nacimiento')
    photo= forms.ImageField(label='Foto',required=False)
    retired=forms.BooleanField(label='Retirado', required=False)
    class Meta:
        model = Director
        fields = ['name','films','birth','photo','retired']

class WindowsForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    tittle =forms.CharField(max_length=100,label='Titulo')
    picture = forms.ImageField(label='Imagen')
    text =forms.CharField(max_length=10000,label='Contenido')
    class Meta:
        model = Windows
        fields = ['name','tittle','picture','text']
    

