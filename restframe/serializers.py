from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='')
    class Meta:
        model = Book
        fields = ['url', 'id', 'name', 'price']
