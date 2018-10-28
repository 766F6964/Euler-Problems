def gen_triangles(limit):
    k = 1
    while k <= limit:
        yield sum(range(k + 1))
        k += 1

def count_divisors(x):
    n = 0
    for i in range(1, int(x ** 0.5 + 1)):
        if x % i == 0:
            n += 1
    return n * 2

def find_number():
    for x in gen_triangles(100000):
        if count_divisors(x) >= 500:
            return x

print(find_number())