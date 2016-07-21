# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TennisApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='forename',
        ),
        migrations.AddField(
            model_name='player',
            name='surname',
            field=models.CharField(default='Doe', max_length=100),
        ),
    ]
