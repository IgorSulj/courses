from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import BookList
app_name = 'restframe'

urlpatterns = [
    path('', BookList.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
