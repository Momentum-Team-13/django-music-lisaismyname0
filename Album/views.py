from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "Album/list_albums.html", {"albums": albums})


def album_info(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "Album/album_info.html", {"album": album})


def add_album(request):
    if request.method == "GET":
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums.html")
    return render(request, "Album/add_album.html", {"form": form})
