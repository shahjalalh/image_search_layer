from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.URLField(max_length=255)
    snippet = models.TextField()
    thumbnail = models.TextField()
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.snippet


class ImageSearch(models.Model):
    term = models.CharField(max_length=255)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term
