import random

print("The Number Guessing Game")

number = random.randint(1,9)

chances = 0

print("Guess A Number Between 1 and 9")

while chances < 5:
    guess = int(input("Enter Your Guess:-"))
    if guess == number:
         print("Congratulation You Won!!!!")
         break
    elif guess < number:
        print("Your Guess Was Too Low: Guess a number higher than", guess)
    else:
        print("Your Guess Was Too High: Guess A Number Lower Than", guess)
    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The Number Is", number)
  
