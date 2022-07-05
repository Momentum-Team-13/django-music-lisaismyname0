from django import forms
from .models import Album
from .models import Favorite


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "artist",
            "name",
            "favorite"
        ]
        labels = {
            "artist": "artist",
            "album": "album",
        }


class FavoriteForm(forms.ModelForm):
    model = Favorite
    fields = [
        "favorite"
    ]
    labels = {
        "favorite": "⭐",
    }
