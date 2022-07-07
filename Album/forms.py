from django import forms
from .models import Album
from .models import Favorite


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "artists",
            "name",
        ]
        labels = {
            "artists": "Artists:",
            "name": "Album Title:",
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            "user",
            "album",
        ]
