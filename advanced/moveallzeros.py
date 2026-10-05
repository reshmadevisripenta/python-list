numbers = [0, 1, 0, 3, 12, 0, 5]

result = [x for x in numbers if x != 0]
result += [0] * numbers.count(0)

print(result)