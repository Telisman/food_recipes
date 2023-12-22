from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe_text', 'ingredients', 'author']
class RecipeRatingForm(forms.Form):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rate this recipe (1-5)')


class RecipeSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Recipes', required=False)
    min_ingredients = forms.IntegerField(label='Minimum Ingredients', required=False)
    max_ingredients = forms.IntegerField(label='Maximum Ingredients', required=False)