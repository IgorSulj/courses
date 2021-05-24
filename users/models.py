from django.db.models import *

# Create your models here.


class User(Model):
    name = CharField(max_length=150)

    def __str__(self):
        return self.name


class Comment(Model):
    user = ForeignKey(User, on_delete=CASCADE, blank=True)
    content = CharField(max_length=255)
    date_created = DateTimeField(auto_now_add=True)

