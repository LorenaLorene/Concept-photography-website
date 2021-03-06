# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-11 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us_page_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonials', tinymce.models.HTMLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutusfrontpage',
            name='testimonials',
        ),
        migrations.AlterField(
            model_name='aboutusfrontpage',
            name='description_field',
            field=models.CharField(max_length=1000),
        ),
    ]
