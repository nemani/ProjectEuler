def dig_set(k):
    sett=set()
    for i in str(k):
        sett.add(i)
    return sett
for a in range(1,1000000):
    if dig_set(a) == dig_set(2*a) and dig_set(a) == dig_set(3*a) and dig_set(a) == dig_set(4*a) and dig_set(a) == dig_set(5*a) and dig_set(a) == dig_set(6*a):
        print "Solution to Euler 52 is:", a 
        break