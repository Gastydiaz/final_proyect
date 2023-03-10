# Generated by Django 4.1.3 on 2023-01-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movies_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='creation',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='studio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='studio_image'),
        ),
        migrations.AddField(
            model_name='studio',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ubicacion'),
        ),
    ]
