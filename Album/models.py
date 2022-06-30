from django.db import models
from django.utils import timezone


class Album(models.Model):
    artist_name = models.CharField(max_length=255)
    track_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    added_to_database_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album_name}"
