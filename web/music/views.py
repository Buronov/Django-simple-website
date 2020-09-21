from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from music.models import Album, Song
from .forms import AlbumForm

def home(request):
	return render(request, 'index.html')

def album_list(request):
	queryset = Album.objects.all()
	context= {
		'albums': queryset
	}
	return render(request, 'album_list.html', context)

def album_detail(request, id=None):
	queryset = get_object_or_404(Album, id=id)
	context = {
		'instance': queryset
	}
	return render(request, 'album_detail.html', context)


def AlbumCreate(request):
	form = AlbumForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/music/albums/')
	context = {
		'form': form
	}
	return render(request, 'Album_create.html', context)


def Album_update(request, id=None):
	instance = get_object_or_404(Album, id=id)
	form = AlbumForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/music/albums/')
	context = {
		'form': form,
		'instance': instance
	}
	return render(request, 'Album_create.html', context)

def album_delete(request, id=None):
	instance = get_object_or_404(Album, id=id)
	instance.delete()
	return HttpResponseRedirect('/music/albums/')

