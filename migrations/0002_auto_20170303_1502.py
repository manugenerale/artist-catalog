# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artiste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='url_image',
            field=models.ImageField(upload_to='/static/artiste/static/img/'),
        ),
        migrations.AlterField(
            model_name='oeuvre',
            name='url_oeuvre',
            field=models.ImageField(upload_to='/static/artiste/static/img/'),
        ),
    ]