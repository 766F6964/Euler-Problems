def largest_prime_factor():
    value, div = 600851475143, 2
    while value > 1:
        while value % div == 0:
            value /= div
            yield div
        div += 1

print(max(largest_prime_factor()))