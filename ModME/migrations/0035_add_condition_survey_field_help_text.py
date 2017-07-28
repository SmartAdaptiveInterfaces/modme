# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-28 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModME', '0034_add_default_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='surveys',
            field=models.ManyToManyField(blank=True, help_text=b'Hold down "Control", or "Command" on a Mac, to <em>de</em>select one.<br/>', to='ModME.Survey'),
        ),
    ]