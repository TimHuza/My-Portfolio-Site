from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.courses_list, name='courses'),
]