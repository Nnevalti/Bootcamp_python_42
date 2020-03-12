from book import Book
from recipe import Recipe

book = Book("La cuisine pour les nuls")

tourte = Recipe("Mugcake", 1, 5, ["Farine", "Oeuf", "Chocolat", "Lait"], "This is a quick and easy dessert to make", "dessert")
tarte = Recipe("Boeuf bourguignon", 3, 240, ["Boeuf", "Carotte", "Vin rouge", "Spice"], "Spécialités Bourguignonne", "lunch")
avocat = Recipe("Avocat a la Mayonnaise", 1, 10, ["Avocat", "Mayonnaise"], "", "starter")
b = Recipe("Btest", 1, 10, ["Avocat", "Mayonnaise"], "", "starter")
c = Recipe("Ctest", 1, 10, ["Avocat", "Mayonnaise"], "", "starter")
t = Recipe("Ttest", 1, 10, ["Avocat", "Mayonnaise"], "", "starter")

# print("Create book : ",book.name, book.creation_date, book.last_update)
book.add_recipe(tourte)
book.add_recipe(tarte)
Recipe.cb()
book.add_recipe(avocat)
book.add_recipe(b)
book.add_recipe(c)
book.add_recipe(t)
Recipe.cb()

# book.get_recipe_by_name("Tourte")
# book.get_recipe_by_name("Tarte")
book.get_recipe_by_name("Doesn't exist")
book.get_recipes_by_types("starter")
print(Recipe.cb.__doc__)
