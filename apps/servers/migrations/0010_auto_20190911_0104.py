# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-11 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0009_auto_20190909_0903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipmodel',
            options={'permissions': (('view_IP', 'can view IP'),)},
        ),
        migrations.AlterModelOptions(
            name='networkdevicemodel',
            options={'ordering': ['id'], 'permissions': (('view_networkDevice', 'can view networkDevice'),)},
        ),
    ]
