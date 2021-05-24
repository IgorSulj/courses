from django.db import models

# Create your models here.


class CourseModel(models.Model):
    name = models.CharField(max_length=150)
    persons = models.ManyToManyField('PersonModel', related_name='courses')

    def __str__(self):
        return self.name


class PersonModel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ProfileModel(models.Model):
    person = models.OneToOneField(PersonModel, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField()

    def __str__(self):
        return f'{self.person}({self.age}) profile'


