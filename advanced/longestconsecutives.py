numbers = [100, 4, 200, 1, 3, 2]

numbers = sorted(set(numbers))

longest = []
current = []

for i in range(len(numbers)):
    if i == 0 or numbers[i] == numbers[i - 1] + 1:
        current.append(numbers[i])
    else:
        current = [numbers[i]]

    if len(current) > len(longest):
        longest = current.copy()

print("Longest sequence:", longest)