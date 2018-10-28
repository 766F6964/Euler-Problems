def find_pythagorean_triplet():
    n = 1000
    for a in range(1, n // 2):
        for b in range(a + 1, n):
            c = n - a - b
            if a * a + b * b == c * c and a + b + c == n:
                return a * b * c

print(find_pythagorean_triplet())