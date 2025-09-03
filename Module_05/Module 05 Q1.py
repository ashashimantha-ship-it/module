import random
dice = int(input("How many dice to roll: "))
rolls = []
for _ in range(dice):
    rolls.append(random.randint(1, 6))
print("Sum of the dice:", sum(rolls))