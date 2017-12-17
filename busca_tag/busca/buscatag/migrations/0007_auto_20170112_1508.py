# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscatag', '0006_auto_20170112_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetolist',
            name='nome',
        ),
        migrations.AddField(
            model_name='projetolist',
            name='nome',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buscatag.Pessoa'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='projetolist',
            name='tag',
        ),
        migrations.AddField(
            model_name='projetolist',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='buscatag.Tag'),
            preserve_default=False,
        ),
    ]