numbers = [10, 20, 10, 30, 10, 40]

given = 10
count = 0

for x in numbers:
    if x == given:
        count = count + 1

print("Occurrences:", count)