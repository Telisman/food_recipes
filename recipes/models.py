from django.db import models
from user.models import User
from ingredient.models import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    recipe_text = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
