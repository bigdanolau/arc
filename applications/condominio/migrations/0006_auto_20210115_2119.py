# Generated by Django 3.1.4 on 2021-01-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0005_auto_20201216_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condominio',
            name='id_apartamento',
        ),
        migrations.AddField(
            model_name='condominio',
            name='numero_meses',
            field=models.IntegerField(default=1),
        ),
    ]
