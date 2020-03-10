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
		print('add')
	elif option == '2' :
		print("delete")
	elif option == '3' :
		print("Please enter the recipe's name to get its details:")
		str = input()
		find(str)
	elif option == '4' :
		print_cookbook()
	elif option == '5' :
		exit()
	else :
		print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")
