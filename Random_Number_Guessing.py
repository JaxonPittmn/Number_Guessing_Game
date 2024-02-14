import random

num = random.randint(0, 100)
i = 1
while i < 11:
  guess = int(input(f"Attempt {i}/10: Guess a number 0 - 100: "))
  print(" ")
  while guess < 0 or guess > 100:
    guess = int(input("Try again, guess a number 0 - 100: "))
  else:
    if guess == num:
      print("Good job")
      print(" ")
      break
    elif guess > num:
      print("Less")
      print(" ")
    elif guess < num:
      print("More")
      print(" ")
  i += 1
print("You Failed")