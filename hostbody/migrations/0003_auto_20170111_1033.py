# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostbody', '0002_groupinfo_hostinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinfo',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='group',
            field=models.ManyToManyField(blank=True, to='hostbody.GroupInfo'),
        ),
        migrations.AlterField(
            model_name='hostinfo',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]