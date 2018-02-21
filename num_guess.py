import random

ran_num = random.randint(1,10)

print "I'm thinking of a number between one and ten."
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
