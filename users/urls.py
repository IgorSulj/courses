from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import CommentView

app_name = 'users'

urlpatterns = [
    path('api/', CommentView.as_view(), name='api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
