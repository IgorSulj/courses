from django.contrib import admin
from .models import Person, Photos, Album, ImgAlbum
# Register your models here.

admin.site.register(Person)
admin.site.register(Photos)
admin.site.register(Album)
admin.site.register(ImgAlbum)

