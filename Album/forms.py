from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "artist_name",
            "track_name",
            "album_name",
        ]
