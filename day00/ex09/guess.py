import random

print("This is an interactive game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

number = random.randint(1,99)
ntry = 0

while 1 :
	guess = input("What's your guess between 1 and 99?\n")
	ntry += 1
	if (guess.isdigit()) :
		if (int(guess) == number) :
			if (number == 42) :
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if (ntry == 1) :
				print("Congratulations! You got it on your first try!")
			else :
				print("You won in %d attempt" % ntry)
			exit()
		elif (int(guess) > number) :
			print("Too high!")
		else :
			print("Too low")
	elif guess == "exit" :
		print("Goodbye!")
		exit();
	else :
		print("That's not a number")
