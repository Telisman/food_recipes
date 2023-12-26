from django.db import models
from user.models import User
from ingredient.models import Ingredient


#model for are Recipe's
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    recipe_text = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)  # To store average rating
    total_ratings = models.PositiveIntegerField(default=0)
    def __str__(self):
            return self.name

#Rating model for are recipe's
class RecipeRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'recipe')

    def save(self, *args, **kwargs):
        if self.recipe.author != self.user:
            super(RecipeRating, self).save(*args, **kwargs)


            ratings = RecipeRating.objects.filter(recipe=self.recipe)
            total_ratings = ratings.count()
            average_rating = sum(rating.rating for rating in ratings) / total_ratings if total_ratings > 0 else 0
            self.recipe.average_rating = average_rating
            self.recipe.total_ratings = total_ratings
            self.recipe.save()