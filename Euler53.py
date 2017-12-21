from math import factorial as ft
def c(n,r):
    return float(ft(n))/(ft(r)*ft(n-r))
ans = 0
for n in range(1,101):
    for r in range(1,n):
        if c(n,r)>1000000:
            ans+=1
print ans