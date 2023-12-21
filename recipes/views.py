from django.shortcuts import render, redirect
from .form import RecipeForm
from django.contrib.auth.decorators import login_required
@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Assuming you're using user authentication
            recipe.save()
            return redirect('create_recipe')  # Replace 'home' with the desired redirect URL after recipe creation
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})
