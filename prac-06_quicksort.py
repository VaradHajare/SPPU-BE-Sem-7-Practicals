# Analysis of Quick Sort: Deterministic vs Randomized pivot

import random
import time
import sys

sys.setrecursionlimit(10000)    # sorted input makes deterministic quick sort go deep
count = 0                       # counts comparisons


def quick_sort(arr, randomized):
    global count
    if len(arr) <= 1:
        return arr

    if randomized:
        i = random.randint(0, len(arr) - 1)      # random element as pivot
    else:
        i = len(arr) - 1                         # last element as pivot
    pivot = arr[i]
    rest = arr[:i] + arr[i + 1:]

    left = []
    right = []
    for x in rest:
        count += 1
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left, randomized) + [pivot] + quick_sort(right, randomized)


def run(title, data, show_array):
    global count
    print("\n" + title)
    for randomized in (False, True):
        count = 0
        start = time.perf_counter()
        result = quick_sort(data.copy(), randomized)
        t = time.perf_counter() - start
        if randomized:
            name = "Randomized   "
        else:
            name = "Deterministic"
        print(name, ": comparisons =", count, ", time =", round(t, 5), "sec")
        if show_array:
            print("   Sorted array:", result)


# Part 1: user input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
if len(arr) != n:
    print("Number of elements does not match n")
    sys.exit()

print("Original array:", arr)
run("Part 1: Your input", arr, True)

# Part 2: analysis on a large array (worst case for deterministic = sorted input)
size = 1000
data = [random.randint(1, 10000) for i in range(size)]

print("\n--- Part 2: Analysis with", size, "elements ---")
run("Random input", data, False)
run("Sorted input", sorted(data), False)
run("Reverse sorted input", sorted(data, reverse=True), False)