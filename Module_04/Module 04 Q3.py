smallest = None
largest = None

while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    number = float(entry)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest:.1f}")
    print(f"Largest number: {largest:.1f}")