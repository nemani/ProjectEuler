from Euler import prime_sieve
import time
L = 10000
start = time.time()
sett=set()
k = set()
for z in prime_sieve(L):
    k.add(z)
for i in xrange(9,L,2):
    if i not in k:
        for b in xrange(1,i):
            if i-2*(b**2) in k:
                sett.add(i)
        if i not in sett:
            print i, time.time() - start
            break
