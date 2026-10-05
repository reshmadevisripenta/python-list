numbers = [25, 10, 45, 30, 15]

smallest = numbers[0]

for x in numbers:
    if x < smallest:
        smallest = x

print("Smallest:", smallest)