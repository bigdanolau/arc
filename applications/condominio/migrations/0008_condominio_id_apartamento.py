# Generated by Django 3.1.4 on 2021-01-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0007_auto_20210115_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='id_apartamento',
            field=models.TextField(default='', max_length=10),
        ),
    ]
