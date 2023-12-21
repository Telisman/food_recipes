from django.core.management.base import BaseCommand
from ingredient.models import Ingredient
import pandas as pd

class Command(BaseCommand):
    help = 'Add ingredient from an Excel file'

    def handle(self, *args, **kwargs):
        excel_file_path = "ingredient.xlsx"
        df = pd.read_excel(excel_file_path)

        for index, row in df.iterrows():
            ingredient = Ingredient.objects.create(
                name=row['name'],
            )
            self.stdout.write(self.style.SUCCESS(f"Added Ingredient: {ingredient.name}"))
