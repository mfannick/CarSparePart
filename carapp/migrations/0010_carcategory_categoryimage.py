# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-07 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0009_auto_20191107_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcategory',
            name='categoryImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category/'),
            preserve_default=False,
        ),
    ]
