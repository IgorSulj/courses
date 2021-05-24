from django.db.models import *

# Create your models here.


class Category(Model):
    name = CharField(max_length=150, verbose_name='Название')
    slug = SlugField(max_length=150, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(Model):
    category = ForeignKey(Category, on_delete=CASCADE, related_name='category', verbose_name='Категория')
    name = CharField(max_length=150, verbose_name='Название')
    slug = SlugField(max_length=150, verbose_name='Слаг')
    description = TextField(verbose_name='Описание')
    price = FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Teacher(Model):
    name = CharField(max_length=150, verbose_name='ФИО')
    specialization = CharField(max_length=150, verbose_name='Специальность')
    photo = ImageField(upload_to='teachers/%Y/%m', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

