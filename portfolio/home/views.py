from django.shortcuts import render
from projects.models import Project
from courses.models import Course

def home_view(request):
    projects = Project.objects.all()
    courses = Course.objects.all()
    context = {
        'projects': projects,
        'courses': courses,
    }
    return render(request, 'home/home.html', context)