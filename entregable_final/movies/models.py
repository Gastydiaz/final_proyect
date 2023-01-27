from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    type = models.CharField(max_length=100, verbose_name='Genero')
    duration = models.FloatField(verbose_name='Duracion')
    picture = models.ImageField(upload_to='movie_images',null=True, blank=True)
    premiered = models.BooleanField(verbose_name='Estrenada', default=True)
    date = models.DateField(null=True, blank=True, verbose_name='Fecha de estreno')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

class Studio(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    creation = models.DateField(null=True, blank=True, verbose_name='Fecha de creacion')
    place = models.CharField(null=True, blank=True, max_length=100, verbose_name='Ubicacion') 
    image = models.ImageField(upload_to='studio_image',null=True, blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    films= models.FloatField(verbose_name='Peliculas')
    birth= models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    photo = models.ImageField(upload_to='director_image',null=True, blank=True)
    retired =models.BooleanField(verbose_name='Retirado', default=False)

    def __str__(self):
        return self.name
