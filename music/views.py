# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Album, Song
from django.shortcuts import render, get_object_or_404
# from django.template import loader
# from django.http import HttpResponse, Http404

def index(request):
    albums = Album.objects.all()
    # context = { "albums":albums }
    return render(request, 'music/index.html', { "albums":albums })

def detail(request, album_id):
    album = get_object_or_404(Album,id=album_id)
    return render(request, 'music/detail.html', { "album":album })

def favorite(request, album_id):
    album = get_object_or_404(Album,id=album_id)
    try:
        song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', { 
            "album":album,
            "error_message":"You Did not select a vaild song", 
            })
    else:
        song.is_favorite = True
        song.save()
        return render(request, 'music/detail.html', { "album":album })