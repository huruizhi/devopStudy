# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-05 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_auto_20190905_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(db_index=True, help_text='主机名', max_length=15, verbose_name='主机名'),
        ),
    ]