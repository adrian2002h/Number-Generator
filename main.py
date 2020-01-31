import random

number = input('Guess a number between 1 and 10\n')

x = random.randint(1, 11)

if x == number:
  print("you guesed right")
else: 
  print("You guess Incorrect")
  print("The number was:", x)

