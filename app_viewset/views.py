from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet
from .models import ProfileModel, CourseModel
from .serializers import ProfileSerializer, CourseSerializer

# Create your views here.


class ProfileListView(ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


class CourseViewSet(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(detail=False)
    def step_by_two(self, request):
        courses = self.get_queryset()[::2]
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)
