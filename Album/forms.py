from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "artist",
            "name",
        ]
        labels = {
            "artist": "artist",
            "album": "album",
        }


class FavoriteForm(forms.ModelForm):
    fields = [
        "favorite",
    ]
    labels = {
        "favorite": "⭐",
    }
