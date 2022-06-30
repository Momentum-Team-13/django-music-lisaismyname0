from django.db import models
from django.utils import timezone
from users.models import User


class Album(models.Model):
    artist_name = models.CharField(max_length=255)
    track_name = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    added_to_database_at = models.DateTimeField(
        auto_now_add=True,)

    def __str__(self):
        return f"{self.album_name}"


class Artist(models.Model):
    artist_name = "artist_name"
    artists_albums = ["artist_album1", "artist_album2"]

    album = models.ForeignKey(
        "Album", on_delete=models.CASCADE, related_name="artist", blank=True, null=True)

    def __str__(self):
        return f"{self.artist_name}"


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorites")
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="favorites")
