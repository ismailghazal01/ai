from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        for recipe in self.recipes_list[recipe_type]:
            print(recipe.name)

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Error")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()