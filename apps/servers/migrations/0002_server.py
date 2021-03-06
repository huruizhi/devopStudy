# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-04 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0001_initial'),
        ('idc', '0001_initial'),
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, help_text='管理IP', max_length=15, unique=True, verbose_name='管理IP')),
                ('hostname', models.CharField(db_index=True, help_text='主机名', max_length=15, unique=True, verbose_name='主机名')),
                ('cpu', models.CharField(help_text='cpu', max_length=50, verbose_name='cpu')),
                ('mem', models.CharField(help_text='mem', max_length=50, verbose_name='mem')),
                ('disk', models.CharField(help_text='disk', max_length=50, verbose_name='disk')),
                ('os', models.CharField(blank=True, help_text='disk', max_length=50, null=True, verbose_name='disk')),
                ('sn', models.CharField(help_text='sn', max_length=50, unique=True, verbose_name='sn')),
                ('rmt_card_ip', models.CharField(help_text='远程管理卡IP', max_length=15, unique=True, verbose_name='远程管理卡IP')),
                ('cabinet_position', models.CharField(blank=True, help_text='机柜内位置', max_length=20, null=True, verbose_name='机柜内位置')),
                ('uuid', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='uuid')),
                ('last_check', models.DateField(auto_now=True, help_text='检测时间', verbose_name='检测时间')),
                ('Idc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='idc.Idc', verbose_name='Idc 机房')),
                ('cabinet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cabinet.Cabinet', verbose_name='所在机柜')),
                ('manufacturer', models.ForeignKey(help_text='制造商', on_delete=django.db.models.deletion.CASCADE, to='servers.Manufacturer', verbose_name='制造商')),
                ('model_name', models.ForeignKey(help_text='服务器型号', on_delete=django.db.models.deletion.CASCADE, to='servers.ProductModel', verbose_name='服务器型号')),
            ],
            options={
                'db_table': 'resource_server',
                'ordering': ['id'],
            },
        ),
    ]
