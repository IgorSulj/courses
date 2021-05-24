from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

app_name = 'rocket'

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)