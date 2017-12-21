sett=set()
for n in range(1,10000):
    k = n*(3*n-1)/2
    sett.add(k)
for a in sett:
    for b in sett:
        if a+b in sett:
            if a-b in sett:
                print a,b , a-b
                break
                break
                