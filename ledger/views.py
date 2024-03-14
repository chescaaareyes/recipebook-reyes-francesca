from django.shortcuts import render
from .models import Ingredient, Recipe, RecipeIngredient

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'ledger/recipes_list.html', ctx)

def recipe(request, pk):
    recipe_name = Recipe.objects.get(pk=pk)
    ingredients = RecipeIngredient.objects.filter(recipe__pk=pk)
    ctx = {
        'recipe': recipe_name,
        'ingredients': ingredients
    }
    return render(request, 'ledger/recipe.html', ctx)