numbers = [25, 10, 45, 30, 15]

largest = numbers[0]

for x in numbers:
    if x > largest:
        largest = x

print("Largest:", largest)