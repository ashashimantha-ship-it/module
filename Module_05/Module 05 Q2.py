numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
top_five = numbers[:5]

print("The greatest numbers in descending order:")
for num in top_five:
    print(num)