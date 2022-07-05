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
            "favorite": "Mark as favorite ⭐"
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            "favorite"
        ]
        labels = {
            "favorite": "⭐",
        }
