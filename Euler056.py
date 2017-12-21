def dig_sum(k):
    summ=0
    for i in str(k):
        summ+=int(i)
    return summ

ans = 0    
for a in range(101):
    for b in range(101):
        t = dig_sum(a**b)
        if t > ans:
            ans = t
print "solution to Euler 56 is:",ans