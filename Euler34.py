from math import factorial
def sum_f(k):
    p=0
    for i in str(k):
        p+= factorial(int(i))
    return p
ans = 0
for i in range(10,1000000):
    if i == sum_f(i):
        ans+=i
print "sloution to euler 34 is:",ans