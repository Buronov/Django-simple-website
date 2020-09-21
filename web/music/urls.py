from django.urls import path, include
from music.views import home, album_list, album_detail, AlbumCreate, Album_update, album_delete

urlpatterns = [
	path('music/', home, name='homepage'),
	path('music/albums/', album_list, name='album_list'),
	path('music/albums/<int:id>/' , album_detail, name='album_detail'),
	path('music/albums/create/', AlbumCreate, name='album_create'),
	path('music/albums/edit/<int:id>/' , Album_update, name='album_edit'),
	path('music/albums/<int:id>/delete/' , album_delete, name='album_delete'),
]

  