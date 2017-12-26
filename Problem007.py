def is_prime(n):
    if n == 2 or n == 3: return 1
    if n % 2 == 0 or n < 2: return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def find_10001_prime():
    n, k = 0, 0
    while k < 10001:
        n += 1
        if is_prime(n):
            k += 1      
    return n

print(find_10001_prime())