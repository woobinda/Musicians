# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_auto_20160523_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(
                blank=True, null=True, upload_to=b'user_avatars'),
        ),
    ]