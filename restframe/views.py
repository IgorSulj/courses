from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
# Create your views here.


def book(request):
    return HttpResponse('Hello')


class BookList(APIView):

    def get(self, request):
        usernames = BookSerializer(Book.objects.all(), many=True, context={'request': request})
        return Response(usernames.data)
