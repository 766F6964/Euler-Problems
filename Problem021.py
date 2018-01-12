def get_divisors(n):
    sum = 1
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            sum += i
            sum += n / i
    return sum


def find_amicable_pair():
    total = 0
    for x in range(1, 10001):
        a = get_divisors(x)
        b = get_divisors(a)
        if b == x and x != a:
            total += x
    return total


print(find_amicable_pair())