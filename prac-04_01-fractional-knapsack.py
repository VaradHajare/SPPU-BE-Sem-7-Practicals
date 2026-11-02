# 0-1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))
name = []
profit = []
weight = []

for i in range(n):
    name.append(chr(65 + i))                          # A, B, C, ...
    profit.append(int(input("Profit of " + name[i] + ": ")))
    weight.append(int(input("Weight of " + name[i] + ": ")))

W = int(input("Enter knapsack capacity: "))

# dp[i][w] = best profit using first i items with capacity w
dp = [[0] * (W + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        if weight[i - 1] <= w:                        # item i can fit: include or exclude
            dp[i][w] = max(dp[i - 1][w], profit[i - 1] + dp[i - 1][w - weight[i - 1]])
        else:                                         # item i cannot fit
            dp[i][w] = dp[i - 1][w]

print("\nDP table:")
for i in range(n + 1):
    print(dp[i])

selected = []
w = W
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:                     
        selected.append(name[i - 1])
        w = w - weight[i - 1]

print("\nMaximum profit =", dp[n][W])
print("Items selected =", selected)