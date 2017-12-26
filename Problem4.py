def largest_palindrome():
    for x in range(0, 1000):
        for k in range(0, 1000):
            if(str(x*k) == str(x*k)[::-1]):
                yield x*k

print(max(largest_palindrome()))