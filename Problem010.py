def is_prime(n):
    if n == 2 or n == 3: return 1
    if n % 2 == 0 or n < 2: return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def sum_of_primes():
    n, s = 2000000, 0
    for x in range(2, n):
        if is_prime(x):
            s += x
    return s

print(sum_of_primes())