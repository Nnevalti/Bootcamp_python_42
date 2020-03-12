class Recipe :
	"""This is a recipe"""

	name = ""
	cooking_lvl = 0
	cooking_time = 0
	ingredients = []
	description = ""
	recipe_type = ""
	nb_recipe = 0

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type) :
		if not name == "" :
			self.name = name
		else :
			print("Name is invalid")
			del self
			exit()
		if cooking_lvl >= 1 and cooking_lvl <= 5 :
			self.cooking_lvl = cooking_lvl
		else :
			print("Cooking lvl is invalid")
			del self
			exit()
		if cooking_time > 1 :
			self.cooking_time = cooking_time
		else :
			print("Cooking time is invalid")
			del self
			exit()
		if not ingredients == [] :
			self.ingredients = ingredients
		else :
			print("Ingredients are invalid")
			del self
			exit()
		self.description = description
		if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert" :
			self.recipe_type = recipe_type
		else :
			print("Invalid recipe type")
			del self
			exit()
		Recipe.nb_recipe += 1
		print("Recipe %s was created!" % self.name)

	def __str__(self) :
		"""Return the string to print with the recipe info"""

		txt = "\nName : {}\nCooking Lvl : {}\nCooking time : {}\nIngredients : {}\nDescription : {}\nRecipe type : {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
		return txt

	def how_many(cls):
		"""Display the number of recipe created"""
		print(cls.nb_recipe, "recipes created in total")

	cb = classmethod(how_many)
