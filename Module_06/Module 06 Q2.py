import random

def roll_dice(faces):
    return random.randint(1, faces)
faces = int(input())
while True:
    result = roll_dice(faces)
    print(result)
    if result == faces:
        break