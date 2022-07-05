from django.db import models
from django.utils import timezone


class Album(models.Model):
    name = models.CharField(max_length=255)
    added_to_database_at = models.DateTimeField(
        auto_now_add=True,)
    artist = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="albums", blank=True, null=True)
    # this says given an artist i can show all of the album objects that are related to that artist
    # one to many field (album can have 1 artist, but an artist can have many albums)
    favorite = models.BooleanField(default="True")

    def __str__(self):
        return f"{self.name}"


class Artist(models.Model):
    # related name should be the plural of the model that i'm on
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Favorite(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="favorites")
    favorite = models.BooleanField(default=False)
