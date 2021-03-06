# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostbody', '0006_auto_20170113_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='host',
            field=models.ManyToManyField(blank=True, to='hostbody.HostInfo'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='memo',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u624b\u673a'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token'),
        ),
    ]
