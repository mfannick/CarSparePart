# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0008_auto_20191107_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='sparePart',
            field=models.ManyToManyField(blank=True, null=True, to='carapp.SpareParts'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]