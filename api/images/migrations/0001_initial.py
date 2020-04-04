# Generated by Django 3.0.4 on 2020-04-04 09:59

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/upload',
                                                                                              location='D:\\Utilisateurs\\Ryan\\Documents\\Cours\\IMT\\2eme annee\\Dev Mob\\Projet\\projet-mobile-back\\api\\media/upload'), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ImageResult',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('img_path', models.CharField(max_length=1000)),
                ('score', models.FloatField()),
            ],
        ),
    ]
