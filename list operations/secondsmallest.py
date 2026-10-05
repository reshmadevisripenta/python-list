numbers = [10, 50, 30, 40, 20]

smallest = numbers[0]
second = numbers[0]

for x in numbers:
    if x < smallest:
        second = smallest
        smallest = x
    elif x < second and x != smallest:
        second = x

print("Second smallest:", second)