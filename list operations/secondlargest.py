numbers = [10, 50, 30, 40, 20]

largest = numbers[0]
second = numbers[0]

for x in numbers:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest:", second)