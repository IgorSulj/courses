from django.shortcuts import render, get_object_or_404
from .models import Person, ImgAlbum, Album

# Create your views here.


def index(request):
    persons = Person.objects.all()
    one_img = ImgAlbum.objects.get(pk=1)
    context = {'persons': persons, 'one_img': one_img}
    if request.GET:
        img_pk = request.GET['pk']
        img = ImgAlbum.objects.get(pk=img_pk)
        albums = img.album.all()
        context['owners'] = []
        for album in albums:
            context['owners'].append(album.person)
    return render(request, 'persons.html', context)
