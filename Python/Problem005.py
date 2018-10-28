def greatest_common_divisor(a, b): 
    return b and greatest_common_divisor(b, a % b) or a

def least_common_multiple(a, b): 
    return a * b / greatest_common_divisor(a,b)

def smallest_multiple(k):
    n = 1
    for i in range(1, k + 1):
        n = least_common_multiple(n, i)
    return int(n)

print(smallest_multiple(20))