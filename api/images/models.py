# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.
from api.settings import CNN_IMAGES_ROOT


class Image(models.Model):
    upload_storage = FileSystemStorage(location=CNN_IMAGES_ROOT, base_url='/media/upload')
    file = models.FileField(upload_to='', storage=upload_storage, blank=False, null=False)

    def __str__(self):
        return self.file.name


class ImageResult(models.Model):
    date = models.DateField(auto_now=True)
    img_path = models.CharField(max_length=1000)
    score = models.FloatField()
