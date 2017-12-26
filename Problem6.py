def sum_of_squares(k):
    for x in range(1, k + 1):
        yield x**2

def square_of_sum(k):
    for x in range(1, k + 1):
        yield x

def difference():
    k = 100
    res1 = sum(sum_of_squares(k))
    res2 = sum(square_of_sum(k)) ** 2
    return res2 - res1
        
print(difference())