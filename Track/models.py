from django.db import models
from django.utils import timezone


class Track(models.Model):
    artist = models.CharField(max_length=255)
    track_name = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    created_at = timezone.now()
