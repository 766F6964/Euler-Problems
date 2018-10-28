def count_letters(n):
    units = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4]  # 0-9
    sub20 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]  # 10-19
    tens = [6, 6, 5, 5, 5, 7, 6, 6]  		# 20-90

    if n <= 9:
        return units[n]
    if n <= 19:
        return sub20[n % 10]
    if n <= 99:
        s = n // 10 ** 1 % 10
        if n % 10 == 0:
            return tens[s - 2]
        else:
            return tens[s - 2] + units[n % 10]
    if n <= 999:
        s = n // 100 ** 1 % 100
        if n % 100 == 0:
            return units[s] + 7
        else:
            return units[s] + 10 + count_letters(n % 100)
    if n == 1000:
        return 11

def calc_all_numbers():
    sum = 0
    for x in range(1, 1000 + 1):
        sum += count_letters(x)
    return sum

print(calc_all_numbers())