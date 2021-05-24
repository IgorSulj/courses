from django.shortcuts import render

from .models import Category, Course, Teacher

# Create your views here.


def index(request):
    context = {'categories': Category.objects.all(), 'courses': Course.objects.all()}
    return render(request, 'index.html', context)


def teachers(request):
    return render(request, 'teachers.html', {'teachers': Teacher.objects.all()})
