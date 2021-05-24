from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import index, teachers

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('teachers', teachers, name='teachers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
