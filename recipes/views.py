from django.shortcuts import render, redirect, get_object_or_404
from .form import RecipeForm, RecipeRatingForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeRating
from ingredient.models import Ingredient


@login_required
def create_recipe(request):
    ingredients = Ingredient.objects.all()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            selected_ingredients = request.POST.getlist('ingredients')

            for ingredient_id in selected_ingredients:
                ingredient = Ingredient.objects.get(pk=ingredient_id)
                recipe.ingredients.add(ingredient)
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form, 'ingredients': ingredients})


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


@login_required
def own_recipe_list(request):
    user = request.user
    own_recipes = Recipe.objects.filter(author=user)
    return render(request, 'own_recipe_list.html', {'own_recipes': own_recipes})


@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    user = request.user

    if request.method == 'POST':
        form = RecipeRatingForm(request.POST)
        if form.is_valid():
            rating_value = int(form.cleaned_data['rating'])
            if 1 <= rating_value <= 5:
                if recipe.author != user:
                    existing_rating = RecipeRating.objects.filter(user=user, recipe=recipe).first()
                    if existing_rating:
                        existing_rating.rating = rating_value
                        existing_rating.save()
                    else:
                        new_rating = RecipeRating.objects.create(user=user, recipe=recipe, rating=rating_value)
                        new_rating.save()
    else:
        form = RecipeRatingForm()

    ratings = RecipeRating.objects.filter(recipe=recipe)
    total_ratings = ratings.count()
    average_rating = sum(rating.rating for rating in ratings) / total_ratings if total_ratings > 0 else 0

    return render(request, 'recipe_detail.html', {'recipe': recipe, 'average_rating': average_rating, 'form': form})
