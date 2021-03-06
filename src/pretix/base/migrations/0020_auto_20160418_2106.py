# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 21:06
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0019_auto_20160326_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='quota',
            field=models.ForeignKey(blank=True, help_text='If enabled, the voucher is valid for any product affected by this quota.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quota', to='pretixbase.Quota', verbose_name='Quota'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='answers', to='pretixbase.QuestionOption'),
        ),
    ]
