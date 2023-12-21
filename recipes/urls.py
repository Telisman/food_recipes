
from django.urls import path
from .views import create_recipe,recipe_list,own_recipe_list,recipe_detail

urlpatterns = [
    path('create/', create_recipe, name='create_recipe'),
    path('list/', recipe_list, name='recipe_list'),
    path('own-list/', own_recipe_list, name='own_recipe_list'),
    path('detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
