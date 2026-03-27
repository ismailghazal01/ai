class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not isinstance(name, str) or not name:
            print("Error")
            exit()
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            print("Error")
            exit()
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("Error")
            exit()
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            print("Error")
            exit()
        if not isinstance(description, str):
            print("Error")
            exit()
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("Error")
            exit()

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return (
            "Recipe name: " + self.name + "\n" +
            "Cooking level: " + str(self.cooking_lvl) + "\n" +
            "Cooking time: " + str(self.cooking_time) + "\n" +
            "Ingredients: " + ", ".join(self.ingredients) + "\n" +
            "Description: " + self.description + "\n" +
            "Type: " + self.recipe_type
        )