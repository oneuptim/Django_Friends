# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_frienduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frienduser',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='frienduser',
            name='friend_alias',
        ),
        migrations.AddField(
            model_name='friend',
            name='group',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FriendUser',
        ),
    ]
