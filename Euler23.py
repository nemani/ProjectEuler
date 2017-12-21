import time
from math import sqrt
def d(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if t is a perfect square
    return s
def is_sum(a,b):
    for var in b:
        if a-var in b:
            return True
    return False
start,ans,k=time.time(),0,0
abn=set()
for f in range(1,20163): 
    k+=f
    if f < d(f):
        abn.add(f)
    if is_sum(f,abn):
        ans+=f
p,elapsed =k-ans,(time.time() - start)
print "Solution is %s found in %s seconds" % (p, elapsed)

## in this i learnt what a set is and when to use it
## also should keep caution when using range function! dont always have 0 in it!
