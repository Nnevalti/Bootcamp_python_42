from datetime import datetime
from recipe import Recipe

class Book :
	"""This is a cookbook class"""

	creation_date = datetime.now()
	last_update = datetime.now()
	recipe_list = {
					"starter" : [],
					"lunch" : [],
					"dessert" : []
					}

	def __init__(self, name) :
		self.name = name
		print(self.name, "created at", self.creation_date)

	def get_recipe_by_name(self, name) :
		"""Print a recipe with the name `name` and return the instance"""
		for i in self.recipe_list :
			for j in self.recipe_list[i] :
				if j.name == name :
					print(j)
					return
		print("There is no recipe called", name)

	def get_recipes_by_types(self, recipe_type) :
		"""Get all recipe names for a given recipe_type"""
		if recipe_type in self.recipe_list :
			print(recipe_type, "list :")
			for i in self.recipe_list[recipe_type] :
				print("\t", i.name)
		else :
			print("Sorry", recipe_type, "does not exist in", self.name)

	def add_recipe(self, recipe) :
		"""Add recipe to the book and update last_update"""
		if isinstance(recipe, Recipe) :
			for i in self.recipe_list :
				if recipe.recipe_type == i :
					self.recipe_list[i].append(recipe)
					self.last_update = datetime.now()
			print(recipe.name, "was added to the Book", self.name)
		else :
			print("This is not a Recipe")
