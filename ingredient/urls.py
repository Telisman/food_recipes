# recipes/urls.py
from django.urls import path
from .views import top_ingredients

urlpatterns = [
    path('top-ingredients/', top_ingredients, name='top_ingredients'),
]
