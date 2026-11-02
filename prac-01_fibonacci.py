# Recursive and iterative Fibonacci with complexity analysis


def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

n = int(input("Enter the number of terms: "))

print("Recursive Fibonacci:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\nNon-Recursive Fibonacci:")
fibonacci_iterative(n)

print("\nRecursive Fibonacci:")
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")

print("\nNon-Recursive Fibonacci:")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")