# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 01:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'startup')]),
        ),
    ]
