cookbook = {
				'sandwich' :
				{
						'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
						'meal' : 'lunch',
						'prep_time' : '10'
				},
				'cake' :
				{
						'ingredients' : ['flour', 'sugar', 'eggs'],
						'meal' : 'dessert',
						'prep_time' : '60'
				},
				'salad' :
				{
						'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
						'meal' : 'lunch',
						'prep_time' : '15'
				}
			}
def add_recipe() :
	name = input("Enter the name of the recipe\n")
	nb = input("How many ingredients does the recipe need ?\n")
	if not nb.isdigit() :
		print("Wrong input cancelled")
		return
	ingredient = []
	for i in range (int(nb), 0, -1) :
		new_ing = input("Enter one ingredient :\n")
		ingredient.append(new_ing)
	meal = input("What type of meal is it ?\n")
	time = input("How long does it take to cook ?\n")
	new_recipe = {'ingredients' : ingredient, 'meal' : meal, 'prep_time' : time}
	add = {name : new_recipe}
	cookbook.update(add)
	print(cookbook[name])


def delete_recipe(str) :
	for i in cookbook :
		if i == str :
			del cookbook[i]
			print("%s was deleted" % i)
			return

def find(str) :
	for i in cookbook :
		if i == str :
			print("Recipe for %s:" % str)
			print("Ingredients list:", cookbook[i]['ingredients'])
			print("To be eaten for %s" % cookbook[i]['meal'])
			print("Takes %s minutes of cooking" % cookbook[i]['prep_time'])
			return
	print("Sorry this recipe does not exist.")

def print_cookbook() :
	for i in cookbook :
		print("Recipe for %s:" % i)
		print("Ingredients list:", cookbook[i]['ingredients'])
		print("To be eaten for %s" % cookbook[i]['meal'])
		print("Takes %s minutes of cooking" % cookbook[i]['prep_time'])
		print('\n')

print('Please select an option by typing the corresponding number :')
print('1: Add a recipe')
print('2: Delete a recipe')
print('3: Print a recipe')
print('4: Print the cookbook')
print('5: Quit')
while 1 :
	option = input()
	if option == '1' :
		add_recipe()
	elif option == '2' :
		delete_recipe(input("Please enter the recipe to delete\n"))
	elif option == '3' :
		find(input("Please enter the recipe's name to get its details:\n"))
	elif option == '4' :
		print_cookbook()
	elif option == '5' :
		print("Cookbook closed.")
		exit()
	else :
		print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
