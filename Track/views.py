from django.shortcuts import render
from .models import Track

# Create your views here.


def view_track(request):
    tracks = Track.objects.all()
    return render(request, "Track/track_info.html", {"Track": tracks})
