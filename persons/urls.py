from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import index

app_name = 'persons'

urlpatterns = [
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)