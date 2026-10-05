numbers = [5, -2, 8, -7, 3, -1, 6]

result = [x for x in numbers if x < 0]
result += [x for x in numbers if x >= 0]

print(result)