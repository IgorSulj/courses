from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from .models import ProfileModel, CourseModel
from .serializers import ProfileSerializer, CourseSerializer

# Create your views here.


class ProfileListView(ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


class CourseViewSet(GenericViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        courses = CourseModel.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        course = get_object_or_404(CourseModel, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk):
        course = get_object_or_404(CourseModel, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def partial_update(self, request, pk):
        course = get_object_or_404(CourseModel, pk=pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk):
        course = get_object_or_404(CourseModel, pk=pk)
        course.delete()
        return Response(status=200)

    @action(detail=False, methods=['delete'], url_path='total', url_name='total')
    def destroy_all(self, request):
        courses = CourseModel.objects.all()
        courses.delete()
        return Response(status=200)

    @action(detail=False, methods=['post'], url_path='destroy')
    @destroy_all.mapping.post
    def create_many(self, request):
        serializer = CourseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(serializer.errors, status=400)
