from django.db.models import *

# Create your models here.


class Person(Model):
    name = CharField(max_length=150, verbose_name='Имя')
    surname = CharField(max_length=150, verbose_name='Фамилия')

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Photos(Model):
    person = ForeignKey(Person, on_delete=CASCADE, verbose_name='Человек')
    avatar = ImageField(upload_to='persons/avatar/%Y/%m', verbose_name='Аватар')
    image = ImageField(upload_to='persons/image/%Y/%m')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'


class Album(Model):
    person = ForeignKey(Person, on_delete=CASCADE)
    name = CharField(max_length=100)


class ImgAlbum(Model):
    album = ManyToManyField(Album)
    img = ImageField(upload_to='album/%Y/%m')


class CustomUser(Model):
    login = CharField(max_length=150)
    password = CharField(max_length=150)


class SharingCustomUser(CustomUser):
    age = IntegerField()
    sex = CharField(max_length=1)


class GopUser(SharingCustomUser):
    dev = CharField(max_length=100)
