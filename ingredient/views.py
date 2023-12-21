# recipes/views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Ingredient
from recipes.models import Recipe

def top_ingredients(request):
    top_ingredients = Ingredient.objects.annotate(num_recipes=Count('recipe')).order_by('-num_recipes')[:5]

    return render(request, 'top_ingredients.html', {'top_ingredients': top_ingredients})
