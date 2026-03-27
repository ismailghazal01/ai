from book import Book
from recipe import Recipe

book = Book("book")

r1 = Recipe("cake", 3, 30, ["flour", "eggs"], "good", "dessert")
r2 = Recipe("salad", 1, 10, ["tomato"], "", "starter")

book.add_recipe(r1)
book.add_recipe(r2)

book.get_recipes_by_types("dessert")
book.get_recipe_by_name("cake")