# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='crew_size',
            new_name='space',
        ),
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='family_friendly',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='genre',
            field=models.CharField(blank=True, choices=[('Musical', 'Musical'), ('Opera', 'Opera'), ('Play', 'Play'), ('Ballet', 'Ballet'), ('Classical', 'Classical'), ('Comedy', 'Comedy')], max_length=20, null=True),
        ),
    ]
