# Generated by Django 2.1.7 on 2019-07-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_auto_20190717_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='eliminado',
            field=models.BooleanField(default=False, verbose_name='Eliminado'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]
