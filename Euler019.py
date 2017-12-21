from calendar import weekday
a = 1901
count = 0
while a < 2001:
    b = 1
    while b < 13:
        if weekday(a, b, 1) == 6:
            count += 1
            print a, b
        b += 1
    a += 1


print count