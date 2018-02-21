import random

ran_word = 0
ran_num = random.randint(1,10)

# Converts ran_num from int to str.
if ran_num == 1:
  ran_word = "one"
elif ran_num == 2:
  ran_word = "two"
elif ran_num == 3:
  ran_word = "three"
elif ran_num == 4:
  ran_word = "four"
elif ran_num == 5:
  ran_word = "five"
elif ran_num == 6:
  ran_word = "six"
elif ran_num == 7:
  ran_word = "seven"
elif ran_num == 8:
  ran_word = "eight"
elif ran_num == 9:
  ran_word = "nine"
elif ran_num == 10:
  ran_word = "ten"

print "I'm thinking of a number between one and ten."
guess = raw_input("Take a guess at what it might be: ")

if type(guess) == int:
  if guess == ran_num:
    print "Correct."
  elif guess < ran_num:
    print "Wrong. Too low."
    print "I was thinking of " + str(ran_num) + "."
  elif guess > ran_num:
    print "Wrong. Too high."
    print "I was thinking of " + str(ran_num) + "."
elif type(guess) == str:
  if guess.lower() == ran_word:
    print "Correct."
  else:
    print "Sorry, you didn't manage to guess the number I was thinking of correctly."
  
