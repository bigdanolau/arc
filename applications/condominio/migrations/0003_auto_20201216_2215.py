# Generated by Django 3.1.4 on 2020-12-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0002_auto_20201214_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='id_apartamento',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='condominio',
            name='id_usuario',
            field=models.TextField(default='', max_length=10),
        ),
    ]
