import random

play_again = True

print "THIS IS A STABLE RELEASE. AS SUCH, THIS PROGRAM WILL ONLY ACCEPT NUMERICAL INPUTS FOR pick_bound AND guess VARIABLES. CONTACT dev@nvai.com FOR MORE INFORMATION."
print

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
			guess = raw_input("Take a guess at what it might be: ")

	if int(guess) == ran_num:
		print
		print "Correct. I was thinking of the number " + str(ran_num) + "."
	elif int(guess) <= ran_num - 0.5*ran_num:
		print
		print "Ooh, you were way too low."
		print "I was thinking of the number " + str(ran_num) + "."
	elif int(guess) <= ran_num - 0.1*ran_num:
		print
		print "You were very close - just slightly too low."
		print "I was thinking of the number " + str(ran_num) + "."
	elif int(guess) >= ran_num + 0.5*ran_num:
		print
		print "Ooh, you guessed quite high!"
		print "I was thinking of the number " + str(ran_num) + "."
	elif int(guess) >= ran_num + 0.1*ran_num:
		print
		print "Your guess was quite close - just a little too high."
		print "I was thinking of the number " + str(ran_num) + "."

	print

	# Verifies if the user would like to re-run the code
	again = raw_input("Would you like to guess again? ")
	if again.lower() == "no" or again.lower() == "n":
		play_again = False
