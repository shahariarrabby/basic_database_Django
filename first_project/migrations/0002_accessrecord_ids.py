# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='ids',
            field=models.IntegerField(null=True),
        ),
    ]
