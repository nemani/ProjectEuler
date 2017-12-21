import time
def d(n):
        t =[]
        for factor in range(1,n):
                if n % factor == 0:
                    t.append(factor)
        return sum(t)
start = time.time()
s,k=0,[]
for a in range(10001):
    p = d(a)
    if a == d(p) and p<10001 and d(p)<10001 and a!=p:
        k.append(a)
s=sum(k)
elapsed = time.time() - start
print "%s found in %s seconds" % (s,elapsed)