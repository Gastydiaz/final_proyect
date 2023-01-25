# Generated by Django 4.1.3 on 2023-01-24 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_director_delete_successful'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.AlterField(
            model_name='director',
            name='films',
            field=models.FloatField(verbose_name='Peliculas'),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='duration',
            field=models.FloatField(verbose_name='Duracion'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
