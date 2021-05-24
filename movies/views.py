from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import F, Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.renderers import JSONRenderer
from .models import Movie, Director, ProductModel, CountryModel
from .serializers import MovieSerializer, ProductSerializer, CountrySerializer
import requests
from .forms import GitForm
# Create your views here.


def index(request, pk=None):
    if pk:
        movies = Movie.objects.filter(pk=pk)
    else:
        movies = Movie.objects.prefetch_related('genres', 'directed_by').all()
    context = {'movies': movies}
    return render(request, 'movies_list.html', context)


def directors_list(request, pk=None):
    if pk:
        directors = Director.objects.filter(pk=pk)
    else:
        directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, 'directors_list.html', context)


def fact(request):
    a = Movie.objects.get(pk=1)
    a.date_created = F('date_created') + 1
    a.save()
    a.refresh_from_db()
    a.save()
    return HttpResponse('Hello')


class MoviesJson(APIView):

    def get(self, request):
        movies = Movie.objects.prefetch_related('directed_by', 'genres').all()
        a = MovieSerializer(movies, many=True, context={'request': request})
        return Response(a.data)


    def post(self, request):
        a = MovieSerializer(data=request.data)
        a.is_valid()
        a.save()
        return Response(a.data)


def directors_by_movie(request, pk):
    directors = Director.objects.filter(director_movies__pk=pk)
    context = {'directors': directors}
    return render(request, 'directors_list.html', context)

def smth(request):
    def pulls_to_repos(pull_requests):
        repos = []
        urls = []
        for i in pull_requests['items']:
            url = i['repository_url']
            pull_json = {'url': i['pull_request']['html_url'], 'comments': i['comments']}
            if url in urls:
                repos[urls.index(url)]['pulls'].append(pull_json)
                continue
            urls.append(url)
            git_json = requests.get(url).json()
            repo_json = {'name': git_json['name'], 'url': git_json['html_url'], 'stars': git_json['stargazers_count'],
                         'pulls': [pull_json]}
            repos.append(repo_json)
        return repos
    if request.method == 'POST':
        form = GitForm(request.POST)
        form.is_valid()
        pulls = requests.get(f'https://api.github.com/search/issues?q=author:{form.cleaned_data["login"]}+is:merged').json()
        unmerged_pulls = requests.get(f'https://api.github.com/search/issues?q=author:{form.cleaned_data["login"]}+is:unmerged').json()
        merged_repos = pulls_to_repos(pulls)
        unmerged_repos = pulls_to_repos(unmerged_pulls)
        return render(request, 'smth.html', {'form': form, 'repositories': [merged_repos, unmerged_repos]})
    form = GitForm()
    return render(request, 'smth.html', {'form': form})


@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.data, status=400)
    else:
        products = ProductModel.objects.prefetch_related('made_in').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class GetProducts(APIView):

    def get(self, request):
        objects = ProductModel.objects.all()
        serializer = ProductSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


class GenericGetProducts(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


@api_view()
def get_countries(request):
    objects = CountryModel.objects.get(pk=1)
    serializer = CountrySerializer(objects)
    return Response(serializer.data)



