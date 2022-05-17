# Generated by Django 4.0.3 on 2022-05-09 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Agencias',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipioId', models.CharField(max_length=5, verbose_name='Id Municipio')),
                ('municipioDepartamento', models.CharField(max_length=256, verbose_name='Ciudad con departamento')),
            ],
            options={
                'verbose_name': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matter_type', models.CharField(max_length=1, verbose_name='Tipo de petición')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Asuntos',
            },
        ),
    ]
