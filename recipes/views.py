from django.shortcuts import render, redirect, get_object_or_404
from .form import RecipeForm, RecipeRatingForm,RecipeSearchForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeRating
from ingredient.models import Ingredient
from django.db.models import Count, Q

#create now recipe, user must be register and login to do this
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

#recipe's list, user must be register and login to do this with search form
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all() #are model
    search_form = RecipeSearchForm(request.GET)#search form
    min_ingredients = request.GET.get('min_ingredients') #form elements
    max_ingredients = request.GET.get('max_ingredients')#form elements

    # Filter recipes by name, text, and ingredients
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')

        if search_query:
            recipes = recipes.filter(
                Q(name__icontains=search_query) |
                Q(recipe_text__icontains=search_query) |
                Q(ingredients__name__icontains=search_query)
            )

    # Filter by minimum and maximum number of ingredients
    if min_ingredients:
        recipes = recipes.annotate(num_ingredients=Count('ingredients')).filter(num_ingredients__gte=min_ingredients)

    if max_ingredients:
        recipes = recipes.annotate(num_ingredients=Count('ingredients')).filter(num_ingredients__lte=max_ingredients)

    return render(request, 'recipe_list.html', {'recipes': recipes, 'search_form': search_form})

#own recipe's list, user must be register and login to do this
@login_required
def own_recipe_list(request):
    user = request.user
    own_recipes = Recipe.objects.filter(author=user)
    return render(request, 'own_recipe_list.html', {'own_recipes': own_recipes})

#recipe detail by selection title and useing id, user must be register and login to do this
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
