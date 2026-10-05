numbers = [10, 20, 10, 30, 10, 40]

old_value = 10
new_value = 100

for i in range(len(numbers)):
    if numbers[i] == old_value:
        numbers[i] = new_value

print(numbers)