# Generated by Django 3.1.4 on 2021-01-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0005_seguimientomodel_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguimientomodel',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
    ]
