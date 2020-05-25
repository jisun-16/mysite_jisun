# Generated by Django 3.0.5 on 2020-05-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WhatDidYouEat', '0003_content_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(blank=True, upload_to='document/%Y.%m'),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
