from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView

from .models import ProductModel
from .serializers import ProductSerializer
from .views import index, fact, directors_list, MoviesJson, smth, directors_by_movie, get_products, get_countries, \
    GetProducts, GenericGetProducts

app_name = 'movies'

urlpatterns = [
    path('smth', smth, name='smth'),
    path('movies', index, name='index'),
    path('movies/<int:pk>', index, name='movie'),
    path('directors_by_movie/<int:pk>', directors_by_movie, name='directors_by_movie'),
    path('api', MoviesJson.as_view(), name='api'),
    path('api/products/', get_products, name='products'),
    path('api/kicel/', GenericGetProducts.as_view(), name='kicel'),
    path('api/kicel2/', ListCreateAPIView.as_view(
        queryset=ProductModel.objects.all(),
        serializer_class=ProductSerializer,
    ), name='kicel2'),
    path('api/kicel2/<int:pk>', GenericGetProducts.as_view()),
    path('api/countries/', get_countries, name='countries'),
    path('fact', fact, name='fact'),
    path('directors', directors_list, name='directors'),
    path('directors/<int:pk>', directors_list, name='directors'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
