from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'platform', 'language', 'teacher', 'price', 'link')
    list_display = ['name', 'platform', 'teacher', 'price']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)