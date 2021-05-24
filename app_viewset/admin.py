from django.contrib import admin
from .models import PersonModel, ProfileModel, CourseModel
# Register your models here.

admin.site.register(PersonModel)
admin.site.register(ProfileModel)
admin.site.register(CourseModel)
