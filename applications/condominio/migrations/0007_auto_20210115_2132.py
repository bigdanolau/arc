# Generated by Django 3.1.4 on 2021-01-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0006_auto_20210115_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='numero_meses',
            field=models.TextField(default='1'),
        ),
    ]
