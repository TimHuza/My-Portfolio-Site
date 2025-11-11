from django.db import models
from django.utils.safestring import mark_safe


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    detail_description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='project/%Y/%m/%d/', blank=True)
    github_link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
    
    def formatted_description(self):
        """Returns the description with preserved formatting"""
        return mark_safe(self.description.replace('\n', '<br>'))