from django.urls import path
from rest_framework.generics import ListAPIView
from rest_framework.routers import DefaultRouter
from .models import PersonModel
from .views import ProfileListView, CourseViewSet
from .serializers import PersonSerializer

app_name = 'app_viewset'

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

# urlpatterns = [
#     path('profile_list/', ProfileListView.as_view(), name='profile_list'),
#     path('person_list/', ListAPIView.as_view(
#         queryset=PersonModel.objects.all(),
#         serializer_class=PersonSerializer,
#     ), name='person_list'),
# ] + router.urls

urlpatterns = router.urls
