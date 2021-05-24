from django.contrib import admin

from .models import Category, Course, Teacher
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)

admin.site.register(Teacher)

