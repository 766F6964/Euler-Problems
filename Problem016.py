def power_digit_sum(n):
    n, k = str(2 ** n), 0
    for x in range(0, len(n)):
        k += int(n[x])
    return k

print(power_digit_sum(1000))
