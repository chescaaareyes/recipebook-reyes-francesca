from django.urls import path
from .views import recipes_list, recipe_1

urlpatterns = [
  path('recipes/list', recipes_list, name="list"),
  path('recipe/1', recipe_1, name="recipe1"),
]

app_name = "ledger"