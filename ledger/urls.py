from django.urls import path
from .views import recipes_list, recipe_1, recipe_2

urlpatterns = [
  path('recipes/list', recipes_list, name="list"),
  path('recipe/1', recipe_1, name="recipe1"),
  path('recipe/2', recipe_2, name="recipe2")
]

app_name = "ledger"