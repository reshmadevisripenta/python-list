numbers = [10, -5, 0, 20, -10, 0, 15, -2]

positive = 0
negative = 0
zero = 0

for x in numbers:
    if x > 0:
        positive = positive + 1
    elif x < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)