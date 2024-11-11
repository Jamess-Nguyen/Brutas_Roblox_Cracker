from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_combinations, name='generate_combinations'),
    path('user_combinations/', views.display_combinations, name='display_combinations'),
]
