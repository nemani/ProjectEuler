import time
def tau(n):
        sqroot,t = int(n**0.5),0
        for factor in range(1,sqroot+1):
                if n % factor == 0:
                        t += 2
        if sqroot*sqroot == n: t = t - 1
        return t
n=0
start = time.time()
for i in xrange(13000):
    if tau(n)>500:
        k = n
        break
    else:
        n+=i
elapsed = (time.time() - start)
print "result %s returned in %s seconds." % (k,elapsed)