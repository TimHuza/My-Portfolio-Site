from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'detail_description', 'image', 'github_link')
    list_display = ['name', 'slug', 'image', 'github_link']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)