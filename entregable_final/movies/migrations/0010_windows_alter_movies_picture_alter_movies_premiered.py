# Generated by Django 4.1.3 on 2023-01-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_director_birth_director_photo_director_retired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Windows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('tittle', models.CharField(max_length=100, verbose_name='Titulo')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='index_image')),
                ('text', models.CharField(max_length=100, verbose_name='Contenido del index')),
            ],
        ),
        migrations.AlterField(
            model_name='movies',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='premiered',
            field=models.BooleanField(blank=True, default=True, verbose_name='Estrenada'),
        ),
    ]
