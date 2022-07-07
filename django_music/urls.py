"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Album import views as album_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', album_views.list_albums, name="list_albums"),

    path('Album/add_album/', album_views.add_album, name="add_album"),

    path('Album/<int:pk>/detail', album_views.album_info, name="album_info"),

    path('Album/<int:pk>/edit/', album_views.edit_album, name="edit_album"),

    path('Album/<int:pk>/delete/',
         album_views.delete_album,
         name='delete_album'),

    # path('Album/<int:pk>/artist/', album_views.by_artist, name="by_artist",
    #      ),

    path('Album/<int:pk>/favorite/', album_views.add_favorite, name="add_favorite"),

    path('artists/<int:pk>/works', album_views.by_artist, name="by_artist"),

    path('Album/<int:pk>/undo_favorite/',
         album_views.undo_favorite, name="undo_favorite"),
]
