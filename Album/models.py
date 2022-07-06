from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Album(models.Model):
    name = models.CharField(max_length=255)
    added_to_database_at = models.DateTimeField(
        auto_now_add=True,)
    artists = models.ManyToManyField("Artist", related_name="albums")
    # artist = models.ForeignKey(
    #     "Artist", on_delete=models.CASCADE, related_name="albums", blank=True, null=True)
    # this says given an artist i can show all of the album objects that are related to that artist
    # one to many field (album can have 1 artist, but an artist can have many albums)
    # favorite = models.BooleanField(default="True")

    def __str__(self):
        return f"{self.name}"

    def check_if_fave(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self:
                return True


class Artist(models.Model):
    # related name should be the plural of the model that i'm on
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    pass


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE,
                             related_name="favorites", null=True, blank=True)
    album = models.ForeignKey(
        "Album", on_delete=models.CASCADE, related_name="favorites", null=True, blank=True)
    # favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
