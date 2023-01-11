# Generated by Django 4.1.3 on 2023-01-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_successful'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('films', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='successful',
        ),
    ]
