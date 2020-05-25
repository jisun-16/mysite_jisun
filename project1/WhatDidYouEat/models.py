from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Content(models.Model):
    objects=models.Manager()
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField(default=timezone.now)
    body=models.TextField(default='')
    image=models.ImageField(upload_to='images/')
    file=models.FileField(upload_to='document/%Y.%m',blank=True)

class Comment(models.Model):
    objects=models.Manager()
    post=models.ForeignKey('Content', on_delete=models.CASCADE)
    text=models.TextField(default='')
    created_date=models.DateTimeField(default=timezone.now)
