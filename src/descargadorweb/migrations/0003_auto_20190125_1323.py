# Generated by Django 2.1.5 on 2019-01-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descargadorweb', '0002_auto_20190125_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquetededescarga',
            name='paquete',
        ),
        migrations.AddField(
            model_name='paquetededescarga',
            name='paqueteb64',
            field=models.TextField(blank=True, null=True),
        ),
    ]
