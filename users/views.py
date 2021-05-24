from django.shortcuts import render
from rest_framework.views import APIView, Response
# Create your views here.
from .models import Comment
from .serializers import CommentSerializer


class CommentView(APIView):

    def get(self, request):
        objects = Comment.objects.all()
        serializer = CommentSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid()
        serializer.create()
        return Response(serializer.data)
