from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    type = models.CharField(max_length=100, verbose_name='Genero')
    duration = models.FloatField(verbose_name='Duracion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

class Studio(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    films= models.FloatField(verbose_name='Peliculas')

    def __str__(self):
        return self.name
