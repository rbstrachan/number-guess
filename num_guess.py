import random

play_again = True
pick_bound = input("Would you like to pick the numbers I choose from? ").lower()

if pick_bound == "yes" or pick_bound == "y":
  print()
  min = input("Choose a lower bound: ")
  max = input("Choose an upper bound: ")
  print()
  print("Nice pick! I'm thinking of a number between " + min + " and " + max + ".")
else:
  min = 1
  max = 10
  print()
  print("Oh, ok then. I'm thinking of a number between one and ten.")

while play_again:
  ran_num = random.randint(int(min),int(max))
  guess = input("Take a guess at what it might be: ")
  
  if int(guess) == ran_num:
    print()
    print("Correct. I was thinking of the number " + str(ran_num) + ".")
  elif int(guess) <= ran_num - 0.5*ran_num:
    print()
    print("Ooh, you were way too low.")
    print("I was thinking of the number " + str(ran_num) + ".")
  elif int(guess) <= ran_num - 0.1*ran_num:
    print()
    print("You were very close - just slightly too low.")
    print("I was thinking of the number " + str(ran_num) + ".")
  elif int(guess) >= ran_num + 0.5*ran_num:
    print()
    print("Ooh, you guessed quite high!")
    print("I was thinking of the number " + str(ran_num) + ".")
  elif int(guess) >= ran_num + 0.1*ran_num:
    print()
    print("Your guess was quite close - just a little too high.")
    print("I was thinking of the number " + str(ran_num) + ".")

  print()

	# Verifies if the user would like to re-run the code
  again = input("Would you like to guess again? ").lower()
  if again == "no" or again == "n":
    play_again = False
