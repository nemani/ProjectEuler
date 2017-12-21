from math import sqrt
from collections import Counter

listt=[]
for a in range(1,400):
    for b in range(1,400):
        c = sqrt( a**2 + b**2 )
        if c == int(c):
            listt.append(a+b+c)
print Counter(listt)