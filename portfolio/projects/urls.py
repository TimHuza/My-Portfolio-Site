from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add-to-cart/<int:project_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:project_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]