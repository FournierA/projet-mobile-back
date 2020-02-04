# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Image(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name


class ImageResult(models.Model):
    image = models.ForeignKey(
        'Image',
        on_delete=models.CASCADE,
    )
    search = models.ForeignKey(
        'ImageSearch',
        on_delete=models.CASCADE,
        related_name='results'
    )
    score = models.FloatField()


class ImageSearch(models.Model):
    date = models.DateField(auto_now=True)
    client = models.CharField(max_length=30)
