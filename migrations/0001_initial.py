# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_artiste', models.CharField(max_length=30, verbose_name='Nom ')),
                ('prenom_artiste', models.CharField(max_length=30, verbose_name='Prenom  ')),
                ('description', models.CharField(max_length=310, verbose_name='Description  ')),
                ('biographie', models.CharField(max_length=1000, verbose_name='Biographie  ')),
                ('caracteristiques', models.CharField(max_length=400, verbose_name='Caracteristiques  ')),
                ('url_image', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30, verbose_name='Titre ')),
                ('description', models.CharField(max_length=400, verbose_name='Description  ')),
                ('url_oeuvre', models.ImageField(upload_to='img/')),
                ('dimension', models.CharField(max_length=30, verbose_name='Dimension (a x b) ')),
                ('type_oeuvre', models.CharField(max_length=30, verbose_name='Type oeuvre(peinture, photo,etc) ')),
                ('date', models.CharField(max_length=30, verbose_name='Date ')),
                ('artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artiste.Artiste')),
            ],
        ),
    ]