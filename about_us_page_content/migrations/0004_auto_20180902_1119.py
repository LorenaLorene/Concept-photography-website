# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_page_content', '0003_ourteam_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeamDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='assets/images')),
            ],
        ),
        migrations.AlterField(
            model_name='customerserviceteam',
            name='description_field',
            field=models.CharField(max_length=500),
        ),
    ]
