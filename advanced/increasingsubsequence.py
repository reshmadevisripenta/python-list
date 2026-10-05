numbers = [10, 22, 9, 33, 21, 50, 41, 60]

dp = [[x] for x in numbers]

for i in range(len(numbers)):
    for j in range(i):
        if numbers[j] < numbers[i]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [numbers[i]]

result = max(dp, key=len)

print("Longest increasing subsequence:", result)