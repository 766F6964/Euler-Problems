from datetime import date

def count_sundays():
    start = date(1901, 1, 1).toordinal()
    end = date(2000, 12, 31).toordinal()

    for x in range(start, end):
        dt = date.fromordinal(x)
        if dt.weekday() == 6 and dt.day == 1:
            yield 1

print(sum(count_sundays()))