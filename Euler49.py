from itertools import permutations
from Euler import prime_sieve
def perm(k):
    sett = set()
    for z in permutations(str(k)):
        n=""
        for t in z:
            n+=t
        sett.add(int(n))
    return sett
        
k = set(prime_sieve(10000))
for i in k:
    if i > 1000:
        if i+3330 in k and i+3330 in perm(i):
            if i+3330*2 in k and i+3330*2 in perm(i):
                print i, i+3330, i+3330*2