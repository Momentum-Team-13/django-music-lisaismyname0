from django import forms
from .models import Album
from .models import Favorite


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "artists",
            "name",
            # "favorite"
        ]
        labels = {
            "artists": "artists",
            "album": "album",
            # "favorite": "Mark as favorite ⭐"
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            "user",
            "album",
        ]
