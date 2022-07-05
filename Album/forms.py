from django import forms
from .models import Album


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


# class FavoriteForm(forms.ModelForm):
#     fields = [
#         "favorite"
#         "user"
#     ]
#     labels = {
#         "favorite": "⭐",
#     }
