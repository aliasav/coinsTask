# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]