# Generated by Django 3.0.7 on 2020-06-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('adicionado', models.DateField(auto_now_add=True, verbose_name='Adicionado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('eliminado', models.BooleanField(default=False, verbose_name='Eliminado')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['id'],
            },
        ),
    ]
