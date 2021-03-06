# Generated by Django 3.1.4 on 2021-01-26 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seguimiento', '0008_auto_20210126_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('contenido', models.CharField(max_length=100)),
                ('archivo', models.FileField(upload_to='')),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('id_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.seguimientomodel')),
            ],
            options={
                'verbose_name': 'ComentarioModel',
                'verbose_name_plural': 'ComentarioModels',
            },
        ),
    ]
