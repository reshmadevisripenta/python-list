numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for value in numbers:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)