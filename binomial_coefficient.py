# Binomial coefficients and Pascal's triangle using dynamic programming.
# Pascal's rule: C(i, j) = C(i-1, j-1) + C(i-1, j)

def build_triangle(n):
    triangle = []

    for i in range(n + 1):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle


n = int(input("Enter n: "))
k = int(input("Enter k: "))

if n < 0:
    print("Enter a non-negative value of n.")
else:
    triangle = build_triangle(n)

    if 0 <= k <= n:
        print(f"C({n}, {k}) = {triangle[n][k]}")
    else:
        print(f"C({n}, {k}) = 0")

    print("\nPascal's Triangle:")

    width = len(str(max(triangle[-1]))) + 1

    for row in triangle:
        line = "".join(str(x).center(width) for x in row)
        print(line.center(width * (n + 1)))