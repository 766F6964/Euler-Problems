import math

def factorial_digit_sum(n):
    s, n = 0, math.factorial(n)
    while n:
        s += n % 10
        n //= 10
    return s

print(factorial_digit_sum(100))