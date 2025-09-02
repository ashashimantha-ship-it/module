import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
three_digit_code = str(digit1) + str(digit2) + str(digit3)

digit1 = random.randint(1, 6)
digit2 = random.randint(1, 6)
digit3 = random.randint(1, 6)
digit4 = random.randint(1, 6)
four_digit_code = str(digit1) + str(digit2) + str(digit3) + str(digit4)
print(f"3-digit code: {three_digit_code}")
print(f"4-digit code: {four_digit_code}")