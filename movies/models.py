from django.db.models import *


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Movie(Model):
    title = CharField(max_length=150)
    slug = SlugField(max_length=150, unique=True)
    directed_by = ManyToManyField('Director', related_name='director_movies')
    genres = ManyToManyField('Genre')
    date_created = PositiveIntegerField()

    def __str__(self):
        return self.title

    def do_smth(self):
        return 'Что-то'


class Director(Model):
    name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    slug = SlugField(max_length=350)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Genre(Model):
    name = CharField(max_length=150, unique=True)
    slug = SlugField(max_length=150)

    def __str__(self):
        return self.name


class MyManager(Manager):

    def filter(self, *args, **kwargs):
        print('Менеджер прокси')
        return super(MyManager, self).filter(*args, **kwargs)


class ProxyMovie(Movie):
    objects = MyManager()

    class Meta:
        proxy = True

    def fn(self):
        print('Я прокси')


class ProductModel(Model):
    name = CharField(max_length=150)
    price = DecimalField(max_digits=6, decimal_places=2)
    description = TextField(blank=True)
    made_in = ManyToManyField('CountryModel', related_name='products')


class CountryModel(Model):
    name = CharField(max_length=150)
    political_systems = [
        ('Демократия', 'Демократия'), ('Авторитарный', 'Авторитарный'), ('Тоталитарный', 'Тоталитарный')
    ]
    political_system = CharField(max_length=150, choices=political_systems)

    def __str__(self):
        return self.name

