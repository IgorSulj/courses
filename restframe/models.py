from django.db.models import *

# Create your models here.


class Book(Model):
    name = CharField(max_length=150, db_index=True)
    price = DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
