from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_combinations, name='generate_combinations'),
    path('combinations/', views.display_combinations, name='display_combinations'),
    path('driver/', views.web_driver, name='selenium_driver'),

]
