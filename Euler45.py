tset=set()
pset=set()
hset=set()
for n in range(143,100000):
    tset.add(n*(n+1)/2)
    pset.add(n*(3*n-1)/2)
    hset.add(n*(2*n-1))
for a in hset:
    if a in pset:
        if a in tset:
            print a 
            