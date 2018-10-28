def find_multiples():
    sum = 0
    for x in range(0, 1000):
        if(x % 3 == 0 or x % 5 == 0):
            sum += x
    return sum

print(find_multiples())