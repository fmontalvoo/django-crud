# Generated by Django 3.0.7 on 2020-06-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('adicionado', models.DateField(auto_now_add=True, verbose_name='Adicionado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('eliminado', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('autor_id', models.ManyToManyField(to='autor.Autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
