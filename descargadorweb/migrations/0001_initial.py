# Generated by Django 2.1.5 on 2019-01-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cer', models.FileField(upload_to='')),
                ('key', models.FileField(upload_to='')),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
    ]
