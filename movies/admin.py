from django.contrib import admin
from .models import Movie, Director, Genre, ProductModel, CountryModel

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'last_name')}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(ProductModel)
admin.site.register(CountryModel)
