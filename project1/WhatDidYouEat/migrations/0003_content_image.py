# Generated by Django 3.0.5 on 2020-05-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhatDidYouEat', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
