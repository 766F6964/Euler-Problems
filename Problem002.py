def fibonacci_sequence():
    a, b, sum = 0, 1, 0
    while a < 4000000:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum

print(fibonacci_sequence())