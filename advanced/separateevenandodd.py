numbers = [5, 2, 8, 1, 7, 4, 6, 3]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

result = even + odd

print(result)