import random

play_again = True

while play_again:
	pick_bound = True
	while pick_bound:
		pbound = raw_input("Would you like to pick the numbers I choose from? ")
		if pbound.lower() == "yes" or pbound.lower() == "y":
			pick_bound = False
			print
			min = raw_input("Choose a lower bound: ")
			max = raw_input("Choose an upper bound: ")
			
			ran_num = random.randint(int(min),int(max))
			
			print
			print "Nice pick! I'm thinking of a number between " + min + " and " + max + "."
			guess = raw_input("Take a guess at what it might be: ")
		else:
			pick_bound = False
			ran_num = random.randint(1,10)
			print
			print "Oh, ok then. I'm thinking of a number between one and ten."
			print
			guess = raw_input("Take a guess at what it might be: ")

			# Converts guess type from str to int.
			if guess == "one":
				guess = 1
			elif guess == "two":
				guess = 2
			elif guess == "three":
				guess = 3
			elif guess == "four":
				guess = 4
			elif guess == "five":
				guess = 5
			elif guess == "six":
				guess = 6
			elif guess == "seven":
				guess = 7
			elif guess == "eight":
				guess = 8
			elif guess == "nine":
				guess = 9
			elif guess == "ten":
				guess = 10

	if int(guess) == ran_num:
		print
		print "Correct."
	elif int(guess) < ran_num:
		print
		print "Ooh, too low."
		print "I was thinking of " + str(ran_num) + "."
	elif int(guess) > ran_num:
		print
		print "Just a little too high."
		print "I was thinking of " + str(ran_num) + "."

	print

	# Verifies if the user would like to re-run the code
	again = raw_input("Would you like to guess again? ")
	if again.lower() == "no" or again.lower() == "n":
		play_again = False
	else:
		print
		
