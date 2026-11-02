# Fractional Knapsack using Greedy method

n = int(input("Enter number of items: "))
name = []
profit = []
weight = []
ratio = []

for i in range(n):
    name.append(chr(65 + i))                      # A, B, C, ...
    profit.append(float(input("Profit of " + name[i] + ": ")))
    weight.append(float(input("Weight of " + name[i] + ": ")))
    ratio.append(profit[i] / weight[i])

capacity = float(input("Enter knapsack capacity: "))

# Table of given items
print("\nItem\tProfit\tWeight\tProfit/Weight")
for i in range(n):
    print(name[i], profit[i], weight[i], round(ratio[i], 2), sep="\t")

# Sort items by ratio, highest first (bubble sort)
for i in range(n):
    for j in range(n - 1 - i):
        if ratio[j] < ratio[j + 1]:
            for lst in (name, profit, weight, ratio):     # swap in all lists
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Greedy selection
total = 0
print()
for i in range(n):
    if capacity == 0:
        break
    if weight[i] <= capacity:         # whole item fits
        print("Take full item", name[i])
        total = total + profit[i]
        capacity = capacity - weight[i]
    else:                             # take only the part that fits
        fraction = capacity / weight[i]
        print("Take", round(fraction, 2), "of item", name[i])
        total = total + profit[i] * fraction
        capacity = 0

print("\nMaximum profit =", round(total, 2))