# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_field', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='assets/images')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesFrontPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=200)),
                ('description_field', models.CharField(max_length=200)),
            ],
        ),
    ]
