def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
list = [1, 2, 3, 4, 5]
result = sum_of_list(list)
print(f"The sum of the numbers in the list is: {result}")