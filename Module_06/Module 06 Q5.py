def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(list)
print(f"Original list: {list}")
print(f"List with even numbers only: {filtered_list}")