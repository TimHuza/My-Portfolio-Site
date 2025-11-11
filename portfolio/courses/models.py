from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=800)
    slug = models.SlugField(unique=True)
    platform = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name