# Generated by Django 4.1.3 on 2023-01-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movies_options_alter_director_films_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images'),
        ),
        migrations.AddField(
            model_name='movies',
            name='premiered',
            field=models.BooleanField(default=True, verbose_name='Estrenada'),
        ),
    ]