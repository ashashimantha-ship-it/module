import random

number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number (1-10): "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct")
        break